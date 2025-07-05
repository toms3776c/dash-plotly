import pandas as pd
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import plotly.express as px


df_gdp = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_apple_stock.csv")

app = Dash()

app.layout = [
    dcc.Graph(figure=px.line(df_gdp, x="AAPL_x", y="AAPL_y", markers=True, title="Apple Stock"))
]


if __name__ == "__main__":
    app.run(debug=True)
