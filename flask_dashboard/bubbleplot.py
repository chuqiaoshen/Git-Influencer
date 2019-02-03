#######
# Catherine Shen 20190202
# bubble chart with the user github age,followers and the pagerank score
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# initial dash app
app = dash.Dash()

#echo environment variables from instances for mysql login
mysql_host = os.environ['MYSQL_HOST']
mysql_username = os.environ['MYSQL_USERNAME']
mysql_password = os.environ['MYSQL_PASSWORD']

''' TODO:change this part to the right mysql data
# Get DATA from mysql db
connection = pymysql.connect(host = mysql_host,
                             user = mysql_username,
                             password = mysql_password,
                             db = 'rank',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()
#select top 15 users by their pange rank rating'''
#cursor.execute("SELECT user,rank FROM user_rank ORDER BY rank DESC LIMIT 15")
'''data = cursor.fetchall()
#grab username and userrank from data list
user_list = []
temp_list = []
rank_list = []
for i in range(len(data)):
    user_list.append(data[i]['user'])
    temp_list.append(i)
    rank_list.append(float(data[i]['rank']))

# Add columns to the DataFrame to convert model year to a string and
# then combine it with name so that hover text shows both:
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']'''

data = [go.Scatter(
            x = user_github_age,
            y = user_pagerank_score,
            text = user_pagerank_score,  # can I use two (a,b) to show?
            mode='markers',
            marker=dict(size=1.5*user_followers_number)
    )]
layout = go.Layout(
    title='PageRank Score vs. User github Age',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubbleChart.html')
