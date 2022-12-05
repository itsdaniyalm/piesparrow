## pieSparrow Typography include

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