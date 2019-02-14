
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

def archive_to_hdfs():
    # code that writes our data from github archive to hdfs

def clean_data():
    # code that clean data downloaded using hdfs

def cleandata_to_hdfs(config, ds, **kwargs):
    # code that writes store our cleaned data into hdfs
    # ds: the date of run of the given task.
    # kwargs: keyword arguments containing context parameters for the run.

def get_hdfs_config():
    #return HDFS configuration parameters required to store data into HDFS.
    return None

config = get_hdfs_config()

dag = DAG(
  dag_id='data_injestion_dag',
  description='data injestion from github archive -> clean -> save to hdfs',
  default_args=default_args)

archive_hdfs = PythonOperator(
  task_id='archive_to_hdfs',
  python_callable=archive_to_hdfs,
  dag=dag)

clean = PythonOperator(
  task_id='clean_data',
  python_callable=clean_data,
  op_kwargs = {'config' : config},
  provide_context=True,
  dag=dag
)

cleandata_hdfs= PythonOperator(
  task_id='cleandata_to_hdfs',
  python_callable=cleandata_to_hdfs,
  dag=dag)

spark_job = BashOperator(
  task_id='spark_task_etl',
  bash_command='spark-submit --master spark_job.py',
  dag = dag)

# setting dependencies
archive_hdfs >> clean >> cleandata_hdfs >> spark_job
