import pandas as pd
import piesparrow as ps

df = pd.read_csv('mock-data.csv')

ps.init(filename='mock-dashboard', title='Mock Dashboard - pieSparrow', basetheme=ps.dark, charttheme=ps.sparrow_dark)

ps.row(
        ps.colxl(ps.h1('Mock Dashboard')+ps.p('This dashboard was developed inside Python to demonstrate the functionality of piesparrow'), align='center')
)
ps.row(
    ps.colxl(ps.h2('These are KPI Visuals'), align='center')
)
ps.row(
        ps.colxs(ps.kpi(df=df, column='Data 1'), type='card', align='center')+
        ps.colxs(ps.kpi(df=df, column='Data 2'), type='card', align='center')+
        ps.colxs(ps.kpi(df=df, column='Data 3'), type='card', align='center')+
        ps.colxs(ps.kpi(df=df, column='Data 4'), type='card', align='center')+
        ps.colxs(ps.kpi(df=df, column='Data 5'), type='card', align='center')
)
ps.row(
    ps.collg((ps.h2('This is Bar Chart')+ps.chart(type="bar",title='barchart', df=df, columns=['Month','Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5'], xcolumn='Month', height=350)), type='card', align='left')+
    ps.colxs(
        ps.h2('These are Gauges')+
        ps.gauge(title='gauge1', label='Gauge 1', value=55, color='#f44336', height=175)+
        ps.gauge(title='gauge2', label='Gauge 2', value=78, color='#8fce00', height=175),
        type='card',align='left'
    )
)