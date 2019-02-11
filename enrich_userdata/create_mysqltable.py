'''
this python script is for creating table in mysql database
#location and company info use VARCHAR 1000 in this script
'''
import os
import pandas as pds
import pymysql

#echo environment variables from instances for mysql login
mysql_host = os.environ['MYSQL_HOST']
mysql_username = os.environ['MYSQL_USERNAME']
mysql_password = os.environ['MYSQL_PASSWORD']


if __name__ == "__main__":
    table_list = ['C','Cplus','Csharp','Go','Java','JavaScript','Perl','PHP','Python','Python','Ruby','Scala','Shell']
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

    #create table for mysql database
    try:
        for tablename in table_list:
        #select top 2 users by their pange rank rating
            cursor.execute("CREATE TABLE IF NOT EXISTS {}
                                    ('user_name' varchar(255) NOT NULL,
                                    'user_rank' INT,
                                    'user_type' varchar(255),
                                    'github_age' INT,
                                    'followers_num' INT,
                                    'following_num' INT,
                                    'repo_num' INT,
                                    'gist_num' INT,
                                    'location' varchar(1000),
                                    'company' varchar(1000),
                                    PRIMARY KEY ('user_name'))
                                    ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
                                    AUTO_INCREMENT=1;".format(tablename))
    except:
        print('{} table create error,please recheck spelling and query string accuracy'.format(tablename))
