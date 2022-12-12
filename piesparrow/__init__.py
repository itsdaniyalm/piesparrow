#######################################################
# pieSparrow - beta 0.1.0                               #
# developed by - Daniyal M (https://itsdaniyalm.com)  #
# docs - https://piesparrow.itsdaniyalm.com/docs.html #
#######################################################

import pandas as pd
from psptypo import * #Typogrhy module 
from psptable import * #Dataframe module
from psppie import * #Pie Chart Module
from pspdonut import * #Donut Chart Module
from pspgauge import * #Gauge Module
from pspkpi import * #KPI card
from pspchart import * #Multi chart widget (Bar, Line, Spline, Area)

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
    <a href='http://piesparrow.com' title="Made with piesparrow" target="_blank" rel="noopener"><img id="icon" src="http://piesparrow.itsdaniyalm.com/images/icon.png" width="50">
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