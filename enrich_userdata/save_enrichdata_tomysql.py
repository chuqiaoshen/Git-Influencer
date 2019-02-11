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

if __name__ == "__main__":
    # Connect to the mysql database
    connection = pymysql.connect(host='34.208.137.201',
                                 user = 'cat',
                                 password = '1111',
                                 db = 'detail',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    print('mysql db connect sucess')

    for inputfilename in ['C','Cplus','Csharp','Go','Java','JavaScript','Perl','Python','Ruby','Shell', 'Scala']:

        try:
            inputfile_fullpath = inputfilepath + 'userdetail_{}.csv'.format(filename)
            df = pd.read_csv(inputfile_fullpath,usecols = ['user_id', 'user_rank', 'user_type', 'githubage','user_followers', 'user_following', 'repo_num', 'gist_num']) # 'location'])  , 'company'] )
        except:
            print('{} read in files error, please recheck the inputfilepath, make sure inclued '/' at the end'.format(inputfilename))

        try:
            df.to_sql(name=filename,con = connection, if_exists = 'replace', index=False, flavor = 'mysql')
        except:
            print('{} save to mysql db error, make sure your input field match the mysql column type'.format(inputfilename))
