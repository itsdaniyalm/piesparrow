import pandas as pd
import piesparrow as ps

df = pd.read_csv("population.csv")
ps.init(filename='pieChart', title='Example of Pie Chart')
ps.row(
        col1 = ps.h2('Example of a Pie Chart in pieSparrow')
)
ps.row( 
        col1 = ps.table(
                df=df
        )
)
ps.row(
        col1 = ps.pie(
        title = 'Population of Cities',
        dataframe = df,
        labels = 'City',
        data = 'Population 2020',
        height = 400,
        color = ps.dusktilldawn
        ) 
)