![pieSparrow](https://piesparrow.itsdaniyalm.com/images/logo_small.png)

Version - Alpha 0.0.5, Release Date - 27-Nov-22

[Website](https://piesparrow.itsdaniyalm.com) | [Docs](https://piesparrow.itsdaniyalm.com/docs.html) | [Examples](https://piesparrow.itsdaniyalm.com/examples.html) | [GitHub](https://github.com/itsdaniyalm/piesparrow)

---
pieSparrow is a stupidly simple python package to create interactive HTML frontends and dashboards. It is built on top of the robust javascript charting library Chart.js while harnessing the power of light weight Milligram CSS framework for styling and data processing capabilities of Python through Pandas.
![pieSparrow Code](https://piesparrow.itsdaniyalm.com/images/header.png)

## Code in Python deliver in HTML
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

## Simple but flexible layouts
With the power of flexible grids having intuitive rows and columns structure, you can shape your dashboards how ever you want.

```
ps.row (
    col1w = 50,
    col1 = ps.p('This is first column of 50% width')
    col2w = 50,
    col2 = ps.p('This is second column of 50% width')
)
```
## Typography at your service
Write what you want the way you want, four heading sizes and optionality of strong text made simple.

```
ps.row (
    ps.h1('This is H1 Text) +
    ps.h2('This is H2 Text) +
    ps.h3('This is H3 Text) +
    ps.h4('This is H4 Text) +
    ps.p('This is paragraph text') +
    ps.bold('This is bold text')
)
```
## Built in Charts
pieSparrow comes with the capability of charts through javascript out of the box, currently Bar, Line and Pie charts are available with more type being added in upcoming release.
```
df = pd.read_csv('population.csv')
ps.row(
    col1 = ps.pie(
        title = 'Population of Cities',
        dataframe = df,
        labels = 'City',
        data = 'Population 2020',
        height = 400,
        color = ps.rainbow
    )
)
```
---
See the [Website](https://piesparrow.itsdaniyalm.com) , [Docs](https://piesparrow.itsdaniyalm.com/docs.html) or [Examples](https://piesparrow.itsdaniyalm.com/examples.html) to learn more.

---
copyrights © 2022 | developed by [Daniyal M](https://itsdaniyalm.com), released under MIT License.

