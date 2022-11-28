import pandas as pd
import piesparrow as ps

df = pd.read_csv("population.csv")
ps.init(filename='barChart', title='Example of Bar Chart')
ps.row(
    col1 = ps.h2('Example of a Bar Chart in pieSparrow')
)
ps.row( 
        col1 = ps.table(
                df=df
        )
)
ps.row(
        col1 = ps.bar(
            title='Population of Pakistani Cities',
            dataframe = df,
            xlabel = 'City',
            ydata = 'Population 2020',
            ylabel = 'Population in 2020',
            legenddisplay = 'false',
            height= 70,
            color = ps.rainbow
            )
) 
