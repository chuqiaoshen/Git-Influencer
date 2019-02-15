
'''
Data Injestion Pipeline
This airflow data pipeline is for :
1) downloading raw data from github archive to HDFS
2) clean data in HDFS and save cleaned data back to hdfs
3) remove the raw data in HDFS
'''
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
    'start_date': datetime(2019, 1, 24, 12, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@hourly',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

#initial dag object
dag = DAG(
  dag_id='data_injestion_dag',
  description='data injestion from github archive -> extract -> sparkclean and save to hdfs',
  default_args=default_args)

#step1 data download
data_download = BashOperator(
  task_id='data_download',
  bash_command='python /home/ubuntu/data_injestion/download_archive.py',
  dag = dag)

#step2 extract jsonfiles
download_command = "./spark_data_injestion/extract_archive.sh"
if os.path.exists(download_command):
   extract_json = BashOperator(
        task_id= 'extract_json',
        bash_command=download_command,
        dag=dag
   )
else:
    raise Exception("Cannot locate {}".format(create_command))

#step3 get follow relationship
get_follow  = BashOperator(
  task_id='get_follow_relationship',
  bash_command='spark-submit --master get_follow_relationship.py',
  dag = dag)

#step4 get language relationship
get_language = BashOperator(
  task_id='get_language_relationship',
  bash_command='spark-submit --master get_language_relationship.py',
  dag = dag)

# setting dependencies
data_download >> extract_json >> [get_follow, get_language]
