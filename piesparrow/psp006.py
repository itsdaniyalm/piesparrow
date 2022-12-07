#######################################################
# pieSparrow - alpha 0.0.6                            #
# developed by - Daniyal M (https://itsdaniyalm.com)  #
# docs - https://piesparrow.itsdaniyalm.com/docs.html #
#######################################################

import pandas as pd
from psptypo import * #Typogrhy module 
from psptable import * #Dataframe module
from pspbar import * #Bar Chart module
from pspline import * #Line chart module
from psparea import * #Area chart module
from pspspline import * #spline chart module

# Main Themes
lightsparrow = "https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/sparrow-light.css"
local = "billboardjs/sparrow.css"

# Chart Themes
default = "https://cdn.jsdelivr.net/gh/itsdaniyalm/piesparrow-styles@main/default.css"

# Initialization function, must call first before and other functions
def init(filename, title='My pieSparrow page', pagetheme=lightsparrow, charttheme=default, icon=True):
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
    <link rel="stylesheet" href="{pagetheme}">
    <script src="https://cdn.jsdelivr.net/npm/billboard.js@3.6.3/dist/billboard.min.js"></script>
    <title>{title}</title>
    '''
    if icon == True:
        branding = '''
    <img id="icon" src="http://piesparrow.itsdaniyalm.com/images/made.png" width="100">
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

def colxs(content, align='center'):
    start = f'''<div class="col-xs" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colsm(content, align='center'):
    start = f'''<div class="col-sm" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colmd(content, align='center'):
    start = f'''<div class="col-md" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def collg(content, align='center'):
    start = f'''<div class="col-lg" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def colxl(content, align='center'):
    start = f'''<div class="col-xl" align="{align}">'''
    end = f'''</div>'''
    html = start+content+end
    return html

def row(content=()):
    start = '''<div class="row">'''
    end = '''</div>'''
    cont = str(content)
    html = start + cont + end
    file.write(html)