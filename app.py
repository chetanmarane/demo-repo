import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
    external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js",
    ],
    use_pages=True,
    suppress_callback_exceptions=True,
    # server=server
)

# app.title = "UPAg"
# app._favicon = "favicon.png"