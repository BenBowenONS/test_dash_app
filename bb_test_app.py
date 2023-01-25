from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('gap_minder_data.csv')

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1(children='Test app for different hosting options'),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        min = df['year'].min(),
        max = df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={int(year): {'label':str(year)} for year in df['year'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55,
                     range_y = [df['lifeExp'].min(), df['lifeExp'].max()],
                     range_x = [df['gdpPercap'].min(), df['gdpPercap'].max()],
                     )
                     

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(port=8050)