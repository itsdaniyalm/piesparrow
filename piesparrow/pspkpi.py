# pieSparrow Bar Chart include

import pandas as pd

def kpi(df, column):
    last_value = df[column].iat[-1]
    second_last_value = df[column].iat[-2]
    delta = round((last_value - second_last_value),2)
    if delta >0:
        indicator = f'''<h4 style="color:#8fce00">&#9650;{delta}</h4>'''
    else:
        indicator = f'''<h4 style="color:#f44336">&#9660;{delta}</h4>'''
    content = f'''
    <div class="row">
    <p>{column}</p>
    <h1>{last_value}</h1>
    {indicator}
    </div>
  
    '''
    return(content)
