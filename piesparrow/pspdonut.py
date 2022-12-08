# pieSparrow Bar Chart include

import pandas as pd

def donut(title, df, columns, legend='true', legendposition='bottom', height=500):
    z=''
    for column in columns:
        lst = df[column].to_list()
        z = z + f'''"{column}":{lst},'''
    a = '{'+z+'}'
    content = f'''
    <div id="{title}"></div>
    <script>
    var chart = bb.generate({{
        size: {{height:{height}}},
        data: {{
            json: {a} ,
            type: "donut"
        }},
        legend: {{
            show: {legend},
            position: "{legendposition}"
        }},
        bindto:'#{title}'
        }});
    </script>
    '''
    return(content)