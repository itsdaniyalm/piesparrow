import pandas as pd
import piesparrow as ps
from pandasql import sqldf

# import data set and convert Timestamp column to Pandas Data Object with MM-DD-YYYY format
df = pd.read_csv('leads_data.csv')
df['Timestamp'] =  pd.to_datetime(df['Timestamp']).dt.date

# declaring globals for pandasql to work
sql = lambda q: sqldf(q, globals())

# wrangling df to get daily lead count that will be used in line chart
daily_leads = sql('''
SELECT
    Timestamp as Date,
    COUNT(id) as Leads
FROM df 
GROUP BY 1
ORDER BY 1
''')

# wrandling df to get total count of leads 
lead_type = sql('''
SELECT
    TYPE as Type,
    COUNT(id) as Qty
FROM df
GROUP BY 1
''' )

# storing type of leads values as integers that will be later diplayed in dashboard
organic_leads = lead_type.iloc[0,1]
paid_leads = lead_type.iloc[1,1]
total_leads = organic_leads + paid_leads

brands = sql('''
SELECT
    Brand as Brand,
    COUNT(id) as Qty
FROM df
GROUP BY 1
''' )


#initiating pieSparrow html file
ps.init(filename='dashboard', title='Leads Dashboard')

# creating title of dashboard.
ps.row(
    col1=ps.h2('Leads Dashboard'),

)

# creating first row for display with 3 columns to display total, paid and organic leads
ps.row(
    col1w=35,
    col1=(ps.p('Total Leads') + ps.h3(total_leads)),
    col2w=35,
    col2=(ps.p('Organic Leads') + ps.h3(organic_leads)),
    col3w=35,
    col3=(ps.p('Paid Leads') + ps.h3(paid_leads))
)

#creating chart elements, line chart for daily leads and pie chart for brand segmentation
ps.row(
    col1w=50,
    #bar chart for daily lead trends
    col1=ps.bar(
        title='Daily Leads Trend',
        dataframe=daily_leads,
        xlabel='Date',
        ylabel='Leads',
        ydata='Leads',
        height=80,
        color=['#4285F4'],
        legenddisplay='false'
    ),
    col2w=50,
    #pie chart for brands segmentation
    col2=ps.pie(
        title='Brand Segmentation',
        dataframe=brands,
        labels='Brand',
        data='Qty',
        height= 400,
        color= ps.rainbow
    )
)