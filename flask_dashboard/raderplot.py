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

'''TODO change the data source to the target datasource'''
#cursor.execute("SELECT user,rank FROM user_rank ORDER BY rank DESC LIMIT 15")
'''
data = cursor.fetchall()
#grab username and userrank from data list
user_list = []
temp_list = []
rank_list = []
for i in range(len(data)):
    user_list.append(data[i]['user'])
    temp_list.append(i)
    rank_list.append(float(data[i]['rank']))
'''

#create graph object
app.layout = html.Div([dcc.Graph(id='JavaPageRank',
                                 figure = {'data':[go.Scatterpolar(
                                                     r = [user_github_age, user_pagerank_score, user_followers_number],
                                                     theta = ['Github Age','Page Rank Score','Followers Number'],
                                                     fill = 'toself'
                                 )],
                                           'layout':go.Layout(
                                                    polar = dict(
                                                    radialaxis = dict(
                                                    visible = True,
                                                    range = [0, 100]
                                               )
                                             ),
                                             showlegend = False
                                           )}
                                )])


if __name__ == '__main__':
    app.run_server()
