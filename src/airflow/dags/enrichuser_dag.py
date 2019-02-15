#this is the airflow dag for enrich users data and save to MySQL database

# import airflow packages
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
# other packages
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 26, 10, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@hourly',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

#initial dag object
dag = DAG(
  dag_id='enrich_userdata',
  description='enrich data from githubapi -> save enriched data to mysqldb',
  default_args=default_args)

#enrich data from githubapi
t1 = BashOperator(
    task_id='fetch_usersdata',
    bash_command='python3 /home/ubuntu/airflow/airflow/dags/scripts/enrich_user_info.py',
    dag=dag)

#save enriched data to mysqldb
t2 = BashOperator(
    task_id='save_to_mysql',
    bash_command='python3 /home/ubuntu/airflow/airflow/dags/scripts/save_enrichdata_tomysql.py',
    dag=dag)

#dependency
t1 >> t2
