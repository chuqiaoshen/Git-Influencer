# This is the script for running dash app on ubuntu 
pip3 install -r requirements.txt

export MYSQL_HOST='change to MySQL host address'
export MYSQL_USERNAME='change to MySQL username'
export MYSQL_PASSWORD='change to your MySQL password'

python3 app.py
