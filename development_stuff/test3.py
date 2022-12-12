import pandas as pd
import psp006 as ps

df = pd.read_csv('pop_province.csv')

ps.init(filename='layout-test-2', title='Layout Test 2', basetheme=ps.localbase)

ps.row(
    (
        ps.collg(ps.h2('This is Bar Chart'), type='card', align='left')+
        ps.collg(ps.h2('This is Line Chart'), type='card', align='left')
    )
)

ps.row(
    (
        ps.collg(ps.bar(df=df, title='bar', columns=['Year','Sindh', 'Balochistan'], xcolumn='Year'), type='card')+
        ps.collg(ps.line(df=df, title='line', columns=['Year','Sindh'], xcolumn='Year'), type='card')

    )
)

ps.row(
    (
        ps.colmd(ps.h2('This is Pie Chart')+ps.pie(df=df, title='pie', columns=['Balochistan','Sindh','KPK'], height=300), type='card', align='left')+
        ps.colmd(ps.h2('This is DonutChart')+ps.donut(df=df, title='donut', columns=['Balochistan','Sindh','KPK'], height=300), type='card', align='left')
    )
)
ps.row(
    (
        ps.colxs(ps.h2('This is Gauge')+ps.gauge(title='gauge',label='Data', value=56, height=150, color='#6600cc'), type='card', align='left')
    )
)

ps.row(
    (
        ps.colxs(ps.kpi(df=df, column='Balochistan'), type='card', align='center')
    )
)

ps.row(
    (
        ps.collg(ps.table(df=df), type='card', align='center')
    )
)