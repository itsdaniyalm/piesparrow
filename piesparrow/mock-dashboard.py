import pandas as pd
import psp006 as ps

df = pd.read_csv('mock_data.csv')

ps.init(filename='mock-dashboard-dark', title='Mock Dashboard - pieSparrow', basetheme=ps.localdark, charttheme=ps.localsparrowdark)

ps.row(
        ps.colxl(ps.h1('Mock Dashboard')+ps.p('This dashboard was developed inside Python to demonstrate the functionality of pieSparrow'), align='center')
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
    ps.collg((ps.h2('This is Bar Chart')+ps.bar(title='barchart', df=df, columns=['Month','Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5'], xcolumn='Month', height=350)), type='card', align='left')+
    ps.colxs(
        ps.h2('These are Gauges')+
        ps.gauge(title='gauge1', label='Gauge 1', value=55, color='#f44336', height=175)+
        ps.gauge(title='gauge2', label='Gauge 2', value=78, color='#8fce00', height=175),
        type='card',align='left'
    )
)

ps.row(
        ps.colmd(ps.h2('This is Line Chart')+ps.line(df=df, title='line', columns=['Month','Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5'], xcolumn='Month', height=350), type='card',align='left')+
        ps.colmd(ps.h2('This is Donut Chart')+ps.donut(title='donut', df=df, columns=['Month','Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5'], height=350), type='card',align='left')
)

ps.row(
        ps.colmd(ps.h2('This is Pie Chart')+ps.pie(df=df, title='pie', columns=['Month','Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5'],  height=350), type='card',align='left')+
        ps.colmd(ps.h2('This is Area Chart')+ps.area(title='area', df=df, columns=['Month','Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5'], xcolumn='Month',height=350), type='card',align='left')
)

ps.row(
        ps.colmd(ps.h2('This is Spline Chart')+ps.spline(df=df, title='spline', columns=['Month','Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5'], xcolumn='Month', height=400), type='card',align='left')+
        ps.colmd(ps.h2('This is Table showing Dataframe')+ps.table(df=df), type='card',align='left')
)
