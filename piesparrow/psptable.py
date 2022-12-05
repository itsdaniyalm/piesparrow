# pieSparrow table include
import pandas as pd
import re

def table(df):
    tab = df.to_html(index=False)
    chart = re.sub("border=\"1\" class=\"dataframe\"",'',tab)
    chart2 = re.sub("style=\"text-align: right;\"",'',chart)
    return chart2