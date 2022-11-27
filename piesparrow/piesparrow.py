#######################################################
# pieSparrow - alpha 0.0.1                            #
# developed by - Daniyal M (https://itsdaniyalm.com)  #
# docs - https://piesparrow.itsdaniyalm.com/docs.html #
#######################################################

import pandas as pd
import re

# color pallets
default = ["#ff3399","#cc33ff","#6600cc","#3333cc","#330099","#003399","#3366ff","3399ff","33ccff"]
beach = ["#99ccff","#99ffff","#009999","#66cccc","#99cccc","#cc9966","#ffcc99","#ffcccc","#ffffcc"]
forest = ["#333366","#336666","#cc6633","#993300","#99cc66","#999966","#ff6633","#ff9966","#ffcc66"]
dusktilldawn = ["#9999ff","#6666cc","#666699","#333366","#333333","#663300","#996633","#cc9900","#ffcc00"]
rainbow = ["#666699","#3399cc","#66cc99","#99cc99","#ffff99","#ffcc99","#ff9966","#ff6633","#cc3366"]

# Initialization function, must call first before and other functions

def init(filename, title, icon=True):
    head = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
    '''
    global filen
    filen = filename + '.html'
    global file
    file = open(filen,'w')
    file.write(head)
    if icon==True:
        logoHtml='''
        <div><a href='https://piesparrow.itsdaniyalm.com' title="Made with pySparrow" target="_blank" rel="noopener"><img src="https://raw.githubusercontent.com/itsdaniyalm/pysparrow/master/images/new_icon.png" height="30" align="right"></a></div>
        </head>
        <body>
        '''
        file = open(filen,'a')
        file.write(logoHtml)
    else:
        logoHtml='''
        </head>
        <body>
        '''
        file = open(filen,'a')
        file.write(logoHtml)

# H1 text
def h1(txt):
    h1 = f'''
    <h1>{txt}</h1>
    '''
    return h1

# H2 Text
def h2(txt):
    h2 = f'''
    <h2>{txt}</h2>
    '''
    return h2

#H3 Text
def h3(txt):
    h3 = f'''
    <h3>{txt}</h3>
    '''
    return h3

#H4 Text
def h4(txt):
    h4 = f'''
    <h4>{txt}</h4>
    '''
    return h4

# Paragraph Text
def p(txt):
    p = f'''
    <p>{txt}</p>
    '''
    return p

# Bold Text
def bold(txt):
    bold = f'''
    <strong>{txt}</strong>
    '''
    return bold

# Images
def img(path, height=250, width=250):
    image = f'''
    <img src='{path}' width='{width}' height='{height}'>
    '''
    return image

# Bar Chart
def bar(title, dataframe, xlabel, ydata, ylabel, titledisplay = 'true', legenddisplay = 'true', color=default, height = '100', width = '100', grid='false', axis='true'):
    df = f'pd.{dataframe}'
    x_label = dataframe[xlabel].tolist()
    y_data = dataframe[ydata].tolist()
    chart = f'''
    <div><canvas id='{title}' width='{width}' height='{height}'></canvas></div>
    <script>
        const ctx = document.getElementById('{title}');
        new Chart(ctx, {{
          type: 'bar',
          data: {{
            labels: {x_label},
            datasets: [{{
              label: '{ylabel}',
              data: {y_data},
              borderWidth: 0,
              backgroundColor: {color} 
            }}]
          }},
          options: {{
            scales: {{
              y: {{
                beingAtZerop: true,
                display: {axis},
                grid: {{
                  display: {grid}
                }}
            }},
              x: {{
                display: {axis},
                grid: {{
                  display: {grid}
                }}
              }}              
            }},
            plugins: {{
                title: {{
                    align: 'start',
                    display: {titledisplay},
                    text: '{title}'
                }},
                legend: {{
                    display: {legenddisplay}
                }}
            }}
          }}
        }});
      </script>
    '''
    return chart

# Line Chart
def line(title, dataframe, xlabel, ylabel1, ydata1, ylabel2='null', ydata2='null', ylabel3='null', ydata3='null', ylabel4='null', ydata4='null', ylabel5='null', ydata5='null', titledisplay = 'true', legenddisplay = 'true', color=default, height = '100', width = '100', grid='false', axis='true'):
    df = f'pd.{dataframe}'
    x_label = dataframe[xlabel].tolist()
    y_data1 = dataframe[ydata1].tolist()
    try:
        y_data2 = dataframe[ydata2].tolist()
    except:
        y_data2 = 'null'
    try:
        y_data3 = dataframe[ydata3].tolist()
    except:
        y_data3 = 'null'
    try:
        y_data4 = dataframe[ydata4].tolist()
    except:
        y_data4 = 'null'
    try:
        y_data5 = dataframe[ydata5].tolist()
    except:
        y_data5 = 'null'
    chart1 = f'''
    <div><canvas id='{title}' width='{width}' height='{height}'></canvas></div>
    <script>
        const ctxLine = document.getElementById('{title}');
        new Chart(ctxLine, {{
            type: 'line',
            data: {{
                labels: {x_label},
                datasets: [
                {{
                label: ['{ylabel1}'],
                data: {y_data1},
                borderColor: '{color[0]}' 
                }}
    '''
    if y_data2 != 'null':
        chart2 = f'''
                ,{{
                label: ['{ylabel2}'],
                data: {y_data2},
                borderColor: '{color[1]}'
                }}
                '''
    else:
        chart2 = "]},"
    if y_data3 != 'null':
        chart3 = f'''
                ,{{
                label: ['{ylabel3}'],
                data: {y_data3},
                borderColor: '{color[2]}'
                }}
                '''
    else:
        chart3 = "]},"
    if y_data4 != 'null':
        chart4 = f'''
                ,{{
                label: ['{ylabel4}'],
                data: {y_data4},
                borderColor: '{color[3]}'
                }}
                '''
    else:
        chart4 = "]},"
    if y_data5 != 'null':
        chart5 = f'''
                ,{{
                label: ['{ylabel5}'],
                data: {y_data5},
                borderColor: '{color[4]}'
                }}
                '''
    else:
        chart5 = "]},"
    chart6 = f'''
            options: {{
                sscales: {{
              y: {{
                beingAtZerop: true,
                display: {axis},
                grid: {{
                  display: {grid}
                }}
            }},
              x: {{
                display: {axis},
                grid: {{
                  display: {grid}
                }}
              }}              
            }},
                plugins: {{
                    title: {{
                        align: 'start',
                        display: {titledisplay},
                        text: '{title}'
                    }},
                    legend: {{
                        display: {legenddisplay}
                    }}
                }}
            }}
            }});
    </script>
    '''
    chart = chart1 + chart2 + chart3 + chart4 + chart5 + chart6
    return chart

# Pie Chart
def pie(title, dataframe, labels, data, titledisplay = 'true', legenddisplay = 'true', color=default, height = '400', width = '100', grid='false', axis='false'):
    df = f'pd.{dataframe}'
    c_label = dataframe[labels].tolist()
    c_data = dataframe[data].tolist()
    chart = f'''
    <div><canvas id='{title}' width='{width}' height='{height}'></canvas></div>
    <script>
        const ctxpie = document.getElementById('{title}');
        new Chart(ctxpie, {{
          type: 'pie',
          data: {{
            labels: {c_label},
            datasets: [{{
              data: {c_data},
              backgroundColor: {color} 
            }}]
          }},
          options: {{
            maintainAspectRatio: false,
            scales: {{
              y: {{
                beingAtZerop: true,
                display: {axis},
                grid: {{
                  display: {grid}
                }}
            }},
              x: {{
                display: {axis},
                grid: {{
                  display: {grid}
                }}
              }}              
            }},
            plugins: {{
                title: {{
                    align: 'start',
                    display: {titledisplay},
                    text: '{title}'
                }},
                legend: {{
                    display: {legenddisplay}
                }}
            }}
          }}
        }});
      </script>
    '''
    return chart

# Dataframe
def table(df, justify='left'):
    tab = df.to_html(index=False, justify=f'{justify}')
    chart = re.sub("border=\"1\" class=\"dataframe",'',tab)
    return chart

# Grids
def row(col1='False',col2='False',col3='False',col4='False',col5='False', col1w = 100, col2w = 100, col3w = 100, col4w = 100, col5w = 100):
    start = f'''
    <div class = "container">
    <div class = "row">
    '''
    if col1!='False':
        cc1 = f'''<div class="column column-{col1w}">{col1}</div>'''
    else:
        cc1 = ''
    if col2!='False':
        cc2 = f'''<div class="column column-{col2w}">{col2}</div>'''
    else:
        cc2 = ''
    if col3!='False':
        cc3 = f'''<div class="column column-{col3w}">{col3}</div>'''
    else:
        cc3 = ''
    if col4!='False':
        cc4 = f'''<div class="column column-{col4w}">{col4}</div>'''
    else:
        cc4 = ''
    if col5!='False':
        cc5 = f'''<div class="column column-{col5w}">{col5}</div>'''
    else:
        cc5 = ''
    end = '''
    </div>
    </div>
    '''
    html = start+cc1+cc2+cc3+cc4+cc5+end 
    file.write(html)