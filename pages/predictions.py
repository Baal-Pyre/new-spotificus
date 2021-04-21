# Imports from 3rd party libraries
# Imports from this application

# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import model
# Imports from this application

input = int(input())
blah= model(input)

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions
            Select a number between 1 and something else to generate a playlist.
            
            """

        ),
        dcc.Input(
            id="input_range", type="number", placeholder="input with range",
            min=10, max=100, step=3, value=input
        ),
        html.Hr(),
        html.Div(id="number-out"),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.package(blah)
    ]
)




layout = dbc.Row([column1, column2])



