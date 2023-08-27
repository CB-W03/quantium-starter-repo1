import pandas
from dash import Dash, html, dcc
from plotly.express import line

modified_data = pandas.read_csv('modified_daily_sales.csv')
modified_data = modified_data.sort_values(by='date')

dash_app = Dash(__name__)

line_graph = line(modified_data, x='date', y='sales', title='Sales of Pink Morsels at Soul Foods')
data_ui = dcc.Graph(id='visualization', figure=line_graph, style={'color': 'black'})

header = html.H1('Pink Morsel Sales graph', id='header', style={'textAlign': 'center', 'color': 'black'})

dash_app.layout = html.Div([header, data_ui])

if __name__ == '__main__':
    dash_app.run(debug=True)
