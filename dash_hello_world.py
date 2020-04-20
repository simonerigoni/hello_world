# Hello World dash application
# The applicaation can be run stand alone ore within a django web site using django_plotly_dash
# python dash_hello_world.py

import dash
import dash_html_components as html
from django_plotly_dash import DjangoDash

APP_DJANGO_PLOTLY_DASH_NAME = 'dash_hello_world'

def _create_app(django_plotly_dash = False):
    '''
    Creates dash application

    Args:
        django_plotly_dash (boolean): django_plotly_dash or not. Default value False

    Returns:
        app (dash.Dash or DjangoDash): Dash or DjangoDash application
    '''

    if django_plotly_dash == False:
         app = dash.Dash(__name__)
    else:
        app = DjangoDash(APP_DJANGO_PLOTLY_DASH_NAME)

    app.layout = html.Div(children = [
        html.H1(children = 'Hello World!'),
    ])
    return app


if __name__ == '__main__':
    app = _create_app()
    app.run_server(debug = True)
else:
    app = _create_app(django_plotly_dash = True)