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
                             db = 'detail',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()
#select top 15 users by their pange rank rating
cursor.execute("SELECT username FROM Scala ORDER BY user_rank DESC LIMIT 20")
data = cursor.fetchall()
print(data)
