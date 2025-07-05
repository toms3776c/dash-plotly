import pandas as pd
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import plotly.express as px
import dash_bootstrap_components as dbc

df_1 = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_apple_stock.csv")
df_2 = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/auto-mpg.csv")
df_3 = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2010_alcohol_consumption_by_country.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.line(df_1, x="AAPL_x", y="AAPL_y", markers=True)), md=6),
        dbc.Col(dcc.Graph(figure=px.scatter(df_2, x="mpg", y="horsepower")), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.histogram(df_3, x="alcohol")), md=12)
    ])
])


if __name__ == "__main__":
    app.run(debug=True)
