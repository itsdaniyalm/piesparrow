![pieSparrow](https://piesparrow.itsdaniyalm.com/images/logo_button.png) 


Version - 0.1.2, Release Date - 13-Nov-22

![Downloads](https://pepy.tech/badge/piesparrow)]

[Website](https://piesparrow.itsdaniyalm.com) | [Release Notes](https://piesparrow.itsdaniyalm.com/release_notes.html) | [Docs](https://piesparrow.itsdaniyalm.com/docs.html) | [Examples](https://piesparrow.itsdaniyalm.com/examples.html) | [GitHub](https://github.com/itsdaniyalm/piesparrow)

---
piesparrow is a stupidly simple python package to create interactive HTML frontends and dashboards. It is built on top of the javascript charting library Billboard.js while harnessing the power of custom light weight Sparrow CSS framework for styling and data processing capabilities of Python through Pandas.
![pieSparrow Code](https://piesparrow.itsdaniyalm.com/images/header_new.png)

## piesparrow - Code in Python, Present in HTML
Just import pieSparrow into your python script and perform data processingthrough Pandas as usual. When you are ready to visualize, call the relatedfunctions from pieSparrow to design your interactive dashboards and compose the HTML files by running your parent script in Python.

```
import piesparrow as ps

ps.init(filename = 'hello_world', title = 'Hello World !')

ps.row (
    ps.h1('Hello World')
)
```
```
Terminal:
$ python helloWorld.py
```
```
myFolder
|- helloWorld.py
|- hello_world.html
```
## Light and Dark Themes with multiple color options
piesparrow have built in five color themes with both light and dark options, themes can also be customized using external CSS.

![Themes](https://piesparrow.itsdaniyalm.com/images/chart_themes.png) 

## Simple but flexible layouts
With the power of flexible grids having intuitive rows and columns structure, you can shape your dashboards how ever you want.

```
ps.row (
    ps.colsm(ps.h1('This is small column.')) +
    ps.colmd(ps.h1('This is medium column.'))
)
```
## Typography at your service
Write what you want the way you want, four heading sizes and optionality of strong text made simple.

```
ps.row (
    ps.h1('This is H1 Text') +
    ps.h2('This is H2 Text') +
    ps.h3('This is H3 Text') +
    ps.h4('This is H4 Text') +
    ps.p('This is paragraph text') +
    ps.bold('This is bold text') +
    ps.link('https://piesparrow.com','This is a link')
)
```
## Built in Charts
pieSparrow comes with the capability of charts through javascript out of the box, currently Bar, Line, Spline, Area, Pie and Donut charts are available alongside Gauge and KPI visual cards. We keep adding more chart type with new releases.
```
data = pd.read_csv('mock_data.csv')
ps.row (
    ps.chart(
        title = 'myChart',
        df = data,
        columns = ['Month','Data 1'],
        xcolumn = 'Month',
        type = 'bar'
    )
)
```
![Bar Graph](https://piesparrow.itsdaniyalm.com/images/readme_graph.png) 
---
See the [Website](https://piesparrow.itsdaniyalm.com) , [Docs](https://piesparrow.itsdaniyalm.com/docs.html) or [Examples](https://piesparrow.itsdaniyalm.com/examples.html) to learn more.

---
copyrights © 2022 | developed by [Daniyal M](https://itsdaniyalm.com), released under MIT License.

