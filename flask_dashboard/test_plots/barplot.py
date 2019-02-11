"""
Catherine Shen 20180201
Simple dash app with barplot
"""
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pymysql
import pymysql.cursors
import base64

# initial dash app
app = dash.Dash()

#echo environment variables from instances for mysql login
mysql_host = os.environ['MYSQL_HOST']
mysql_username = os.environ['MYSQL_USERNAME']
mysql_password = os.environ['MYSQL_PASSWORD']

# Get DATA from mysql db
connection = pymysql.connect(host = mysql_host,
                             user = mysql_username,
                             password = mysql_password,
                             db = 'rank',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()
#select top 15 users by their pange rank rating
cursor.execute("SELECT user,rank FROM user_rank ORDER BY rank DESC LIMIT 20")
data = cursor.fetchall()
#grab username and userrank from data list
user_list = []
temp_list = []
rank_list = []
for i in range(len(data)):
    user_list.append(data[i]['user'])
    temp_list.append(i)
    rank_list.append(float(data[i]['rank']))

#store color object
colors = {
    'background': '#111111',
    'text': '#003399'
}

#create graph object
app.layout = html.Div([

html.Div(children =
    [
     html.H1(
        children='Git Influencer',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H3(
        children='Help you find people to follow on github for your interest language. ',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Label('Select your interest Language'),
    dcc.Dropdown(
        options=[
            {'label': 'JavaScript', 'value': 'JavaScript'},
            {'label': 'Python', 'value': 'Python'},
            {'label': 'Java', 'value': 'Java'},
        ],
        value=['MTL', 'SF']

    ),
    dcc.Graph(id='user_age_rank_bubble_plot',
                                 figure = {'data':[go.Bar(
                                                   x=user_list,
                                                   y=rank_list,
                                                   opacity=0.7
                                                              )],
                                           'layout':go.Layout(
                                images=[dict(
        source="https://storage.googleapis.com/pics-insight/pagerankcats.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.5, sizey=0.5,
        xanchor="right", yanchor="bottom"
      )],
                                title='User to follow based on pagerank score',
                                xaxis = {'title':'User Github ID'},
                                margin={'l': 100, 'b': 40, 't': 40, 'r': 100},
                                legend={'x': 0, 'y': 1},
                                hovermode='closest')}
                                ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
            options=[
                {'label': 'San Francisco', 'value': 'JavaScript'},
                {'label': 'New York', 'value': 'Python'},
                {'label': 'Seattle', 'value': 'Java'},
            ],
            value=['MTL', 'SF'],
            multi=True
        )]),


    html.Div([
              html.Div([dcc.Graph(id='JavaPageRank',
                                     figure = {'data':[go.Scatterpolar(
                                                         r = [8, 3.4, 5],
                                                         theta = ['Github Age','Page Rank Score','Followers Number'],
                                                         fill = 'toself'
                                     )],
                                               'layout':go.Layout(
                                                        polar = dict(
                                                        radialaxis = dict(
                                                        visible = True,
                                                        range = [0, 10]
                                                   )
                                                 ),
                                                 showlegend = False
                                               )}
                                    )
                                    ]),

            html.Div([
                html.Iframe(src = 'https://storage.googleapis.com/pics-insight/ironman-cats.png', height = 500, width = 500)
            ])
                ])

                ])



if __name__ == '__main__':
    app.run_server()
