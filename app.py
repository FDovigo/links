#>---------------------------------------------------------------------------------------------------<#
#importing packages
#>---------------------------------------------------------------------------------------------------<#

import gunicorn

import dash_bootstrap_components as dbc
from dash import dash, dcc, html
from dash.dependencies import Input, Output, State





##====================================================================================================##
#Essential Functions for Code and App Start
##====================================================================================================##
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SOLAR, dbc.icons.BOOTSTRAP])
server = app.server





##====================================================================================================##
#Varibles and Code Functions
##====================================================================================================##

#Variables
imgFace = "https://raw.githubusercontent.com/FDovigo/imageRepository/main/LinkTree/meNoBG.png"




##====================================================================================================##
#Web Pre-Builds -> Character Sheet
##====================================================================================================##

linkTree = dbc.Container([


    #Cabeçalho1
    dbc.Row([

        dbc.Col([
            

            #Self Image and Name
            html.Img(src = imgFace, style = {"margin-top": "10vh", "height": "20vh"}),
            html.H1("Felipe Dovigo", className = "text-light", style = {"margin-top": "5vh", "text-align": "center", "font-size": "3vh"}),

            html.H1("USP-Lorena", className = "text-body", style = {"margin-top": "2vh", "margin-bottom": "0", "text-align": "center", "font-size": "2vh"}),
            html.H1("Graduação Engenharia de Materiais", className = "text-body", style = {"margin-top": "0vh", "margin-bottom": "0", "text-align": "center", "font-size": "2vh"}),

            #html.H1("USP-ESALQ", className = "text-body", style = {"margin-top": "2vh", "margin-bottom": "0", "text-align": "center", "font-size": "2vh"}),
            #html.H1("Pós-Graduando Engenharia de Software", className = "text-body", style = {"margin-top": "0vh", "margin-bottom": "0", "text-align": "center", "font-size": "2vh"}),


            dbc.Stack([
                    
                dbc.Button([
                    dbc.Nav([
                        dbc.NavItem(
                            dbc.NavLink(html.I(className = "bi bi-instagram"), href = "https://www.instagram.com/f_dovigo/", external_link = True, style = {"color": "#cccccc"})),
                    ], style = {"justify-content": "center"}), 
                ], color = "success", style = {"margin-top": "10vh","font-size": "4vh", "padding": "0"}),
                
                dbc.Button([
                    dbc.Nav([
                        dbc.NavItem(
                            dbc.NavLink(html.I(className = "bi bi-linkedin"), href = "https://www.linkedin.com/in/felipe-dovigo/", external_link = True, style = {"color": "#cccccc"})),
                    ], style = {"justify-content": "center"}), 
                ], color = "success", style = {"margin-top": "10vh","font-size": "4vh", "padding": "0"}),

                dbc.Button([
                    dbc.Nav([
                        dbc.NavItem(
                            dbc.NavLink(html.I(className = "bi bi-github"), href = "https://github.com/FDovigo", external_link = True, style = {"color": "#cccccc"})),
                    ], style = {"justify-content": "center"}), 
                ], color = "success", style = {"margin-top": "10vh","font-size": "4vh", "padding": "0"}),

            ], direction = "horizontal", gap = 5, style = {"justify-content": "center"}),


            html.H1("fcdovigo@usp.br", className = "text-body", style = {"margin-top": "15vh", "text-align": "center", "font-size": "2vh"}),


        ], style = {"width": "80%", "text-align": "center"}, md = 11),

    ], className = "g-0", style = {"justify-content": "center"}),

], fluid = True)



##====================================================================================================##
#Web Layout
##====================================================================================================##


app.layout = dbc.Container([
    linkTree
], className = "g-0", fluid = True, style = {"height": "100vh", "width": "100%", "background": "linear-gradient(0deg, rgba(26,27,39,1) 0%, rgba(57,58,70,1) 100%)"})





##====================================================================================================##
#Web Interactivity
##====================================================================================================##

# @app.callback(
#     Output("left-content", "children"),
#     [
#     Input("url", "pathname")
#     ]
# )

# def render_page(pathname):

#     if pathname == "/" or pathname == "/sharpy":
#         colleft = 6
#         colright = 6
#         return leftSharpy, rightSharpy, colleft, colright
    
#     if pathname == "/backtest":
#         colleft = 7
#         colright = 5
#         return leftBacktest, rightBacktest, colleft, colright
    
#     if pathname == "/strategy":
#         colleft = 8
#         colright = 4
#         return leftStrategy, rightStrategy, colleft, colright





##====================================================================================================##
#Web Interactivity -> Character Sheet
##====================================================================================================##


@app.callback(
    [

    ],

    [

    ]
)

def update(date):


   
    return





##====================================================================================================##
#App Styling
##====================================================================================================##

# @app.callback(
#     Output("nav-collapse", "is_open"),
#     [
#     Input("nav-toggler", "n_clicks")
#     ],
#     [
#     State("nav-collapse", "is_open") 
#     ]
# )

# def toggle_nav_collapse(n, is_open):

#     if n:
#         return not is_open
#     return is_open










##====================================================================================================##
#Other Functions
##====================================================================================================##

if __name__ == "__main__":
    app.run_server(debug = True)
