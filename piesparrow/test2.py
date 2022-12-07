import pandas as pd
import psp006 as ps

df = pd.read_csv('pop_province.csv')

ps.init(filename='layout-test', title='Layout Test', pagetheme=ps.local)

ps.row(
    (
        ps.collg((ps.box(ps.h2('This is bar chart'))), align='left')+
        ps.collg(ps.h2('This is line chart'), align='left')
    )
)
ps.row(
    (
        ps.collg(ps.card(ps.bar(df=df, title='bar', columns=['Year','Sindh', 'Balochistan'], xcolumn='Year')))+
        ps.collg(ps.card(ps.spline(df=df, title='line', columns=['Year','Sindh'], xcolumn='Year')))

    )
)
