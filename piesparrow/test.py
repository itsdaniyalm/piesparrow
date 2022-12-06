import psp006 as ps
import pandas as pd

ps.init(filename='daniyal', title='test')

ps.box(align='center',content=ps.h1(txt='This is Sparta'))

ps.card(
    ps.h4('This is the heading')+
    ps.p(
        'I am trying to'+ps.bold('re write')+'the pieSparrow'
    )
)

df = pd.read_csv('population.csv')

ps.card(content=ps.table(df=df), align='center'
)
