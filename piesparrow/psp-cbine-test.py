import pandas as pd
import psp006 as ps

df = pd.read_csv('pop_province.csv')

ps.init(filename='ps-combine-test', title='Combine Chart Test', pagetheme=ps.local)


ps.card(
        ps.bar(df=df, columns=['Year','Balochistan','KPK','Punjab','Sindh'], xcolumn='Year', title='pop-bar')
    )
ps.row( content=(
    ps.h1('My Title'),
    ps.card(
    ps.line(df=df, columns=['Year','Balochistan'], xcolumn='Year', title='pop-line')
    )
)
)