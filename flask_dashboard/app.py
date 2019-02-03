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
mysql_host = os.environ['mysql_host']
mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']

# Get DATA from mysql db
connection = pymysql.connect(host = mysql_host,
                             user = mysql_username,
                             password = mysql_password,
                             db = 'rank',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()
#select top 15 users by their pange rank rating
cursor.execute("SELECT user,rank FROM user_rank ORDER BY rank DESC LIMIT 15")
data = cursor.fetchall()
#grab username and userrank from data list
user_list = []
temp_list = []
rank_list = []
for i in range(len(data)):
    user_list.append(data[i]['user'])
    temp_list.append(i)
    rank_list.append(float(data[i]['rank']))

#create graph object
app.layout = html.Div([dcc.Graph(id='JavaPageRank',
                                 figure = {'data':[go.Bar(
                                                   x=user_list,  
                                                   y=rank_list
                                                              )],
                                           'layout':go.Layout(
                                title='Java User Page Rank Rating top 15',
                                xaxis = {'title':'User github login name'})}
                                )])


if __name__ == '__main__':
    app.run_server()
