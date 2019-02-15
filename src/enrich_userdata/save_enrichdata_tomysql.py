'''this is the python script to save the userdetail_somelanguage.csv to mysql database
   the tables are already created in mysql 'detail' database
   only ['user_id', 'user_rank', 'user_type', 'githubage','user_followers', 'user_following', 'repo_num', 'gist_num'] will be saved into db
'''

import pymysql
import pymysql.cursors
import pandas as pd

#CHANGE BELOW
inputfilepath  = 'the location of enriched userdetail_{}.csv files '
#CHANGE ABOVE

#echo environment variables from instances for mysql login
mysql_host = os.environ['MYSQL_HOST']
mysql_username = os.environ['MYSQL_USERNAME']
mysql_password = os.environ['MYSQL_PASSWORD']

if __name__ == "__main__":
    # Connect to the mysql database
    connection = pymysql.connect(host= mysql_host,
                                 user = mysql_username,
                                 password = mysql_password,
                                 db = 'detail',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    print('mysql db connect sucess')
    #iterate over the language list for inserting into tables
    for inputfilename in ['C','Cplus','Csharp','Go','Java','JavaScript','Perl','Python','Ruby','Shell', 'Scala']:

        try:
            inputfile_fullpath = inputfilepath + 'userdetail_{}.csv'.format(filename)
            df = pd.read_csv(inputfile_fullpath,usecols = ['user_id', 'user_rank', 'user_type', 'githubage','user_followers', 'user_following', 'repo_num', 'gist_num']) # 'location'])  , 'company'] )
        except:
            print('{} read in files error, please recheck the inputfilepath, make sure inclued '/' at the end'.format(inputfilename))

        try:
            #use df.to_sql to save dataframes into mysql tables
            df.to_sql(name=filename,con = connection, if_exists = 'replace', index=False, flavor = 'mysql')
        except:
            print('{} save to mysql db error, make sure your input field match the mysql column type'.format(inputfilename))
