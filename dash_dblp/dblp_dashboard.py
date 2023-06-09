import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_prep


# read csv and sort by Date to prepare the plot
# df = pd.read_csv("data/earthquakes2.csv", delimiter="\t")
df_cols = ["Year", "Count"]
df = pd.DataFrame(columns=df_cols)

# df = df.sort_values("Date")

# dashboard
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("DBLP - Dashboard", style={"text-align": "center"}),


    dcc.RangeSlider(2000, 2023, 1,
                    count=1,
                    value=[2015, 2023],
                    marks={i: '{}'.format(i) for i in range(2000, 2024, 1)},
                    id="Year_slider"),

    dcc.Dropdown(["Data Science", "Machine Learning", "Deep Learning"], "Data Science", multi=False, id="Keyword"),

# dcc.RangeSlider(0, 20, 1, value=[5, 15], id='my-range-slider'),
#     html.Div(id='output-container-range-slider')

    # dcc.Slider(id="Year",
    #            min=1.1,
    #            max=7.9,
    #            step=0.1,
    #            value=4.5,
    #            marks=None,
    #            tooltip={"placement": "bottom", "always_visible": True}
    #            ),

    # dcc.Dropdown(id="Longitude", figure={}),
    # html.Br(),

    # dcc.Dropdown(id="Latitude", figure={}),
    # html.Br(),

    # html.H1("DBLP - Dashboard", style={"text-align": "center"}),

    dcc.Graph(id="Line_Plot", figure={}),
    html.Br(),

    # dcc.Graph(id="Scatter_Plot", figure={}),
    # html.Br(),
    #
    # dcc.Graph(id="Scatter_Geo", figure={}),
    # html.Br(),
])



@app.callback(
    Output(component_id="Line_Plot", component_property="figure"),
    # Output(component_id="Scatter_Plot", component_property="figure"),
    # Output(component_id="Scatter_Geo", component_property="figure"),
    # Input(component_id="Longitude", component_property="figure"),
    # Input(component_id="Latitude", component_property="figure"),
    Input(component_id="Year_slider", component_property="value"),
    Input(component_id="Keyword", component_property="value")
)
def update_graph(selected, key_value):
    keyword = key_value
    if keyword != "Select Keyword":
        try:
            df = pd.read_csv(f"dash_data/{keyword}.csv")
        except:
            dash_prep.get_data(keyword)
            df = pd.read_csv(f"dash_data/{keyword}.csv")

        dff = df.copy()
        dff = dff[dff["Year"] >= selected[0]]
        dff = dff[dff["Year"] <= selected[1]]

        if len(dff) > 1:
            # Plotly Express
            fig = px.line(dff, x="Year", y="Count",
                          # title="Line-Plot for Keyword:" + keyword,
                          )
            fig.update_layout(title_text="Line-Plot for Keyword:" + keyword, title_x=0.5)
        else:
            dff2 = dff[dff["Year"] == ""]
            fig = px.line(dff2, x="Year", y="Count",
                          # title="Line-Plot for Keyword:" + keyword,
                          )
            fig.update_layout(title_text="Line-Plot for Keyword:" + keyword, title_x=0.5)
            fig.add_annotation(text="Not enough Data available", showarrow=False)

        # fig2 = px.scatter(dff, x="Date", y="Depth", title="Scatter-Plot")
        #
        # if len(dff) <= 0:
        #     fig2.add_annotation(text="Not enough Data available", showarrow=False)
        #
        # fig3 = px.scatter_geo(dff, lat="Latitude", lon="Longitude")
        # return fig, fig2, fig3
        return fig
    else:
        pass


if __name__ == "__main__":
    app.run_server(debug=True)
