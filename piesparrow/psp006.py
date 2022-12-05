#######################################################
# pieSparrow - alpha 0.0.6                            #
# developed by - Daniyal M (https://itsdaniyalm.com)  #
# docs - https://piesparrow.itsdaniyalm.com/docs.html #
#######################################################

import pandas as pd
import re
from psptypo import *
from psptable import *

# color pallets
default = ["#ff3399","#cc33ff","#6600cc","#3333cc","#330099","#003399","#3366ff","3399ff","33ccff"]
beach = ["#99ccff","#99ffff","#009999","#66cccc","#99cccc","#cc9966","#ffcc99","#ffcccc","#ffffcc"]
forest = ["#333366","#336666","#cc6633","#993300","#99cc66","#999966","#ff6633","#ff9966","#ffcc66"]
dusktilldawn = ["#9999ff","#6666cc","#666699","#333366","#333333","#663300","#996633","#cc9900","#ffcc00"]
rainbow = ["#666699","#3399cc","#66cc99","#99cc99","#ffff99","#ffcc99","#ff9966","#ff6633","#cc3366"]

# Initialization function, must call first before and other functions
def init(filename='piesparrow', title='My pieSparrow page', icon=True):
    head = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width", initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="sparrow.css">
        <title>{title}</title>
    '''
    if icon == True:
        branding = '''
        <img id="icon" src="http://piesparrow.itsdaniyalm.com/images/made.png" width="100">
        </head>
        '''
    else:
        branding = '''
        </head>
        '''
    global filen
    filen = filename + '.html'
    global file
    file = open(filen,'w')
    file.write(head+branding)

# box
def box(content, align='left'):
    start = f'''
    <div id="box" align="{align}">
    '''
    end = f'''
    </div>
    '''
    html = start + content + end
    file.write(html)

# card
def card(content, align='left'):
    start = f'''
    <div id="card" align="{align}">
    '''
    end = f'''
    </div>
    '''
    html = start + content + end
    file.write(html)