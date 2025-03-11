# Hello World Dash application
# python dash_hello_world.py

from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello World!")
])

# http://127.0.0.1:8050

if __name__ == '__main__':
    app.run_server(debug = True)
else:
    pass