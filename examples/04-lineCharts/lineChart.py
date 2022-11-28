import pandas as pd
import piesparrow as ps

df = pd.read_csv("pop_province.csv")
ps.init(filename='lineChart', title='Example of Line Chart')
ps.row(
        col1 = ps.h2('Example of a Line Chart in pieSparrow')
)
ps.row( 
        col1 = ps.table(
                df=df
        )
)
ps.row(
        col1 = ps.line(
        title='Population trend of Provinces',
        dataframe= df,
        xlabel = 'Year',
        ylabel1 = 'Balochistan',
        ydata1 = 'Balochistan',
        ylabel2 = 'KPK',
        ydata2 = 'KPK',
        ylabel3 = 'Punjab',
        ydata3 = 'Punjab',
        ylabel4 = 'Sindh',
        ydata4 = 'Sindh',
        height = 70,
        legenddisplay = 'true'
        )
)