import pandas as pd
import psp006 as ps

df = pd.read_csv('mock_data.csv')

ps.init(filename='multi-chart', title='Multi Chart Test', basetheme=ps.localdark, charttheme=ps.localchart)

ps.row(
    ps.chart(
        title='Multi Chart Test',
        df=df,
        columns=['Month','Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5'],
        xcolumn='Month',
        xaxistype='category',
        charttype='bar'
    )
)