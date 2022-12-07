# pieSparrow Bar Chart include

import pandas as pd

def line(title, df, columns, xcolumn, datalabels='true', zoom='true', legend='true', legendposition='bottom', grid='true', xlabel='', ylabel='', height=500):
    z=''
    for column in columns:
        lst = df[column].to_list()
        z = z + f'''{column}:{lst},'''
    a = '{'+z+'}'
    content = f'''
    <div id="{title}"></div>
    <script>
    var chart = bb.generate({{
        size: {{height:{height}}},
        data: {{
            x: "{xcolumn}",
            json: {a} ,
            type: "line",
            labels: {datalabels}
        }},
        zoom: {{
            enabled: {zoom},
            type: "drag"
        }},
        legend: {{
            show: {legend},
            position: "{legendposition}"
        }},
        grid: {{
            x: {{show: true}},
            y: {{show: true}}
        }},
        axis: {{
            x:{{
                label: {{
                    text: "{xlabel}",
                    positon: "outer-center"
                }},
                show: true,
            }},
            y:{{
                label: {{
                    text: "{ylabel}",
                    positon: "outer-center"
                }},
                show: true,
            }}
        }},
        bindto:'#{title}'
        }});
    </script>
    '''
    return(content)