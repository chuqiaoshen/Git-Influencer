'''
this python script is for testing pymysql connectivity and test on SQL queries for Flask
'''
import os
import pandas as pds
import pymysql

#echo environment variables from instances for mysql login
mysql_host = os.environ['MYSQL_HOST']
mysql_username = os.environ['MYSQL_USERNAME']
mysql_password = os.environ['MYSQL_PASSWORD']

if __name__ == "__main__":
    #test mysql connectivity
    try:
        connection = pymysql.connect(host = mysql_host,
                                     user = mysql_username,
                                     password = mysql_password,
                                     db = 'detail',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        print('mysql db connect sucess')
    except:
        print('mysql db connect error, please recheck security group and MYSQL login credentials')

    #test query result
    try:
        topN = 2
        select_table = 'JavaScript'
        #select top 2 users by their pange rank rating
        cursor.execute("SELECT user_id, user_rank, githubage, user_followers,repo_num, gist_num FROM {} ORDER BY user_rank  LIMIT {}".format(select_table,topN))
        data = cursor.fetchall()
        print(data)
    except:
        print('select topN based on rank error')
