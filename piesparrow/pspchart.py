import pandas as pd

def chart(title, df, columns, xcolumn,xaxistype='category', charttype='bar',datalabels='true', zoom='true', legend='true', legendposition='bottom', grid='true', xlabel='', ylabel='', height=500):
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
            x: "{xcolumn}",
            json: {a} ,
            type: "{charttype}",
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
            x: {{show: {grid}}},
            y: {{show: {grid}}}
        }},
        axis: {{
            x:{{
                label: {{
                    text: "{xlabel}",
                    positon: "outer-center"
                }},
                show: true,
                type: "{xaxistype}"
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