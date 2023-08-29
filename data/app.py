import dash
import pandas
from dash import Dash, html, dcc
from plotly.express import line

global_df = pandas.read_csv('modified_daily_sales.csv')
global_df = global_df.sort_values(by='date')

dash_app = Dash(__name__)


def draw_graph(input_data):
    line_graph = line(input_data, x='date', y='sales', title='Sales of Pink Morsels at Soul Foods')
    line_graph.update_layout(plot_bgcolor='lightgrey', font_color='black')
    return line_graph


data_ui = dcc.Graph(id='visualization', figure=draw_graph(global_df))

header = html.H1('Pink Morsel Sales graph',
                 id='header',
                 style={'textAlign': 'center', 'color': 'black', 'border-radius': '20px'})

region = dcc.RadioItems(['north', 'east', 'south', 'west', 'all'], 'all', id='region_choice', inline=True,
                        style={'font-size': '25px'})

region_wrapper = html.Div([region], style={'font_size': '200px'})


@dash_app.callback(dash.Output(data_ui, 'figure'),
                   dash.Input(region, 'value'))
def new_plot(region_choice):
    if region_choice == 'all':
        mod_data = global_df
    else:
        mod_data = global_df[global_df['region'] == region_choice]

    new_graph = draw_graph(mod_data)
    return new_graph
          

dash_app.layout = html.Div([header, region_wrapper , data_ui],
                           style={'textAlign': 'center'})


if __name__ == '__main__':
    dash_app.run(debug=True)

