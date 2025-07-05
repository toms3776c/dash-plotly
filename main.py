import pandas as pd
from dash import Dash, dash_table, dcc, callback, Output, Input, html
import plotly.express as px


df_gdp = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_world_gdp_with_codes.csv")
# df_bar = df_gdp

app = Dash()

app.layout = [
    html.H1("ダッシュボード", style={"textAlign": "center"}),
    dash_table.DataTable(data=df_gdp.to_dict('records'), page_size=10),
    dcc.RadioItems(options=["大きい順", "小さい順"], value="大きい順", id="sort_type"),
    dcc.Graph(figure={}, id="gdp_graph")
]

@callback(
    Output(component_id="gdp_graph", component_property="figure"),
    Input(component_id="sort_type", component_property="value")
)

def update_gdp_graph(value):
    if value == "大きい順":
        df_bar = df_gdp.sort_values(by="GDP (BILLIONS)", ascending=False)[:10]
    else:
        df_bar = df_gdp.sort_values(by="GDP (BILLIONS)", ascending=True)[:10]
    return px.bar(df_bar, x='COUNTRY', y='GDP (BILLIONS)', title="国別GDP")


if __name__ == "__main__":
    app.run(debug=True)
