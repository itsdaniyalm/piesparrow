#######################################################
# pieSparrow - beta 0.1.1                               #
# developed by - Daniyal M (https://itsdaniyalm.com)  #
# docs - https://piesparrow.itsdaniyalm.com/docs.html #
#######################################################

import pandas as pd
import re

# Main Themes
light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/base_light.css"
dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/base_dark.css"
loclight = "billboardjs/base_light.css"
locdark = "billboardjs/base_dark.css"

# Chart Themes
rainbow_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/rainbow_l.css"
rainbow_dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/rainbow_d.css"
sparrow_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/sparrow_l.css"
sparrow_dark="https://cdn.statically.io/gh/itsdaniyalm/piesparrow-styles/main/sparrow_d.css"
virdis_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/virdis_l.css"
virdis_dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/virdis_d.css"
cividis_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/cividis_l.css"
cividis_dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/cividis_d.css"
gold_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/gold_l.css"
gold_dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/gold_d.css"
sunflower_light="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/sunflower_l.css"
sunflower_dark="https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/sunflower_d.css"
locrainbowl = "billboardjs/rainbow_l.css"
locrainbowd= "billboardjs/rainbow_d.css"

# Initialization function, must call first before and other functions
def init(filename, title='My pieSparrow page', basetheme=light, charttheme=sparrow_light, icon=True):
    head = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width", initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600&display=swap" rel="stylesheet">
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <link rel="stylesheet" href="{charttheme}">
    <link rel="stylesheet" href="{basetheme}">
    <script src="https://cdn.jsdelivr.net/npm/billboard.js@3.6.3/dist/billboard.min.js"></script>
    <title>{title}</title>
    <link rel="icon" type="image/x-icon" href="http://piesparrow.itsdaniyalm.com/images/favicon.png">
    '''
    if icon == True:
        branding = '''
    <a href='http://piesparrow.com' title="Made with piesparrow" target="_blank" rel="noopener"><img id="icon" src="http://piesparrow.itsdaniyalm.com/images/icon.png" width="50"></a>
</head>
<body>
        '''
    else:
        branding = '''
        </head>
        <body>
        '''
    global filen
    filen = filename + '.html'
    global file
    file = open(filen,'w')
    file.write(head+branding)

# box
def box(content):
    start = f'''
    <div id="box">
    '''
    end = f'''
    </div>
    '''
    html = start + content + end
    return html

# card
def card(content):
    start = f'''
    <div id="card">
    '''
    end = f'''
    </div>
    '''
    html = start+content+ end
    return html

def colxs(content, align='center', type='box'):
    start = f'''<div id="{type}" class="col-xs" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colsm(content, align='center', type='box'):
    start = f'''<div id="{type}" class="col-sm" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colmd(content, align='center', type='box'):
    start = f'''<div id="{type}" class="col-md" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def collg(content, align='center', type='box'):
    start = f'''<div id="{type}" class="col-lg" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colxl(content, align='center', type='box'):
    start = f'''<div id="{type}" class="col-xl" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def row(content=()):
    start = '''<div class="row">'''
    end = '''</div>'''
    cont = str(content)
    html = start + cont + end
    file.write(html)

def chart(title, df, columns, xcolumn,xaxistype='category', type='bar',datalabels='true', zoom='true', legend='true', legendposition='bottom', grid='true', xlabel='', ylabel='', height=500):
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
            type: "{type}",
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

def gauge(title, label, value, legend='true', legendposition='bottom',color='', height=500):
    content = f'''
    <div id="{title}"></div>
    <script>
    var chart = bb.generate({{
        size: {{height:{height}}},
        data: {{
            columns: [["{label}",{value}]] ,
            type: "gauge"
        }},
        legend: {{
            show: {legend},
            position: "{legendposition}"
        }},
        color: {{
            pattern: ["{color}"]
        }},
        bindto:'#{title}'
        }});
    </script>
    '''
    return(content)

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

def pie(title, df, columns, legend='true', legendposition='bottom', height=500):
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
            type: "pie"
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

def table(df):
    tab = df.to_html(index=False)
    chart = re.sub("border=\"1\" class=\"dataframe\"",'',tab)
    chart2 = re.sub("style=\"text-align: right;\"",'',chart)
    chart3 = '''<div style="overflow-x:auto;">'''+chart2+'''</div>'''
    return chart3

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

# Links
def link(target,label):
    lnk = f'''
    <a href="{target}">{label}</a>
    '''
    return lnk