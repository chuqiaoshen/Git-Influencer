#######
#The final dashboard for dash app
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pymysql
import pymysql.cursors
import os

#initial dash obj
app = dash.Dash()

#lanugages and tables are all named like this list
languages = ['C','Cplus','Csharp','Go','Java','JavaScript','Perl','PHP','Python','Python','Ruby','Scala','Shell']
#initial the app layout
app.layout = html.Div([

        html.H1(
           children='Git Influencer',
           style={
               'textAlign': 'center',
               'color': '#003399'
           }
        ),

        html.H3(
           children='Help you find people to follow on github for your interest language. ',
           style={
               'textAlign': 'center',
               'color': '#003399'
           }
        ),

        html.Label(' Select your interest Language'),
        html.Div([
            dcc.Dropdown(
                id='language',
                options=[{'label': i, 'value': i} for i in languages],
                value='Select your interest language'
            )
        ],
        style={'width': '30%', 'display': 'inline-block'}),

        html.Label('  Select top N user'),
        html.Div([
            dcc.Dropdown(
                id='topN',
                options=[{'label': i, 'value': i} for i in range(5,26)],
                value='Select the top user number'
            )
        ],style={'width': '38%', 'display': 'inline-block'}),

        html.Div(
        'This is an inner Div',
        style={'color':'blue', 'padding':10, 'width':600}
    ),

    dcc.Graph(id='barplot-pagerank')
], style={'padding':10})

#call back function for updating the xaxis and yaxis
@app.callback(
    Output('barplot-pagerank', 'figure'),
    [Input('language', 'value'),
     Input('topN', 'value')])
def update_graph( xaxis_name, yaxis_name):
    mysql_host = os.environ['MYSQL_HOST']
    mysql_username = os.environ['MYSQL_USERNAME']
    mysql_password = os.environ['MYSQL_PASSWORD']

    # Get DATA from mysql db
    connection = pymysql.connect(host = mysql_host,
                                 user = mysql_username,
                                 password = mysql_password,
                                 db = 'detail',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    #select by input
    #select_table,topN = 'Scala', 20
    #select top 2 users by their pange rank rating
    cursor.execute("SELECT user_id, user_rank FROM {} ORDER BY user_rank  LIMIT {}".format(xaxis_name, yaxis_name))
    data = cursor.fetchall()
    #grab username and userrank from data list
    user_list = []
    user_detail_list = []
    normalize_num = int(data[0]['user_rank'])
    for i in range(len(data)):
        user_list.append(data[i]['user_id'])
        user_detail_list.append(float(normalize_num)/(data[i]['user_rank']))

    return {
        'data': [go.Bar(
            x=user_list,
            y=user_detail_list,
            text=user_list,
            opacity= 0.5

        )],
        'layout': go.Layout(
            title='User to follow based on pagerank score',
            xaxis={'title': 'Github Username'},
            yaxis={'title': 'Normalized Pagerank'},
            margin={'l': 60, 'b': 40, 't': 50, 'r': 60},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

if __name__ == '__main__':

    app.run_server()

'''
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
'''
