# pieSparrow Bar Chart include

import pandas as pd

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