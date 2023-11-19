import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash import (
    Input,
    Output,
    State,
    callback,
    ctx,
    html,
    no_update,
    clientside_callback,
)

dash.register_page(__name__, path = "/bar_chart", title="BAR")

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
}

df = pd.DataFrame(data)
# Layout of the app
layout = html.Div([
    html.H1("Bar Chart Example"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': category, 'value': category}
            for category in df['Category']
        ],
        value=df['Category'][0]  # Default value
    ),
    dcc.Graph(id='bar-chart'),

    html.Label("Select a category:"),
    
])

# Callback to update the bar chart based on the selected category
@callback(
    Output('bar-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.bar(filtered_df, x='Category', y='Value', title=f"Bar Chart for {selected_category}")
    return fig

