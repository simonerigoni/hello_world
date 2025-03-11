# Hello World django_plotly_dash application
# python django_plotly_dash_hello_world.py

from dash import Dash, html
from django_plotly_dash import DjangoDash

APP_DJANGO_PLOTLY_DASH_NAME = 'django_plotly_dash_hello_world'

def _create_app(django_plotly_dash = False):
    '''
    Creates dash application

    Args:
        django_plotly_dash (boolean): django_plotly_dash or not. Default value False

    Returns:
        app (dash.Dash or DjangoDash): Dash or DjangoDash application
    '''

    if django_plotly_dash is False:
        app = Dash(__name__)
    else:
        app = DjangoDash(APP_DJANGO_PLOTLY_DASH_NAME)

    app.layout = html.Div(children = [
        html.H1(children = 'Hello World!'),
    ])
    return app

# http://127.0.0.1:8050/

if __name__ == '__main__':
    app = _create_app()
    app.run_server(debug = True)
else:
    app = _create_app(django_plotly_dash = True)