import pandas as pd
import psp006 as ps

df = pd.read_csv('pop_province.csv')

ps.init(filename='ps-bar-test', title='Bar Chart Test')

ps.card(
    ps.bar(df=df, columns=['Year','Balochistan','KPK','Punjab','Sindh'], xcolumn='Year', title='pop')
)
