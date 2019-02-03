import pymysql.cursors
import pandas as pd
# Connect to the mysql database
connection = pymysql.connect(host='ec2-34-208-137-201.us-west-2.compute.amazonaws.com',
                             port = '3306'
                             user='cat',
                             password='1111',
                             db='rank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

df = pd.read_csv('sample_file4.csv',usecols = ['user','rank'] )
df.to_sql(name=rank,con = connection, if_exists = replace, index=False, flavor = 'mysql')
'''
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `rank` (`username`, `rank`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()'''
