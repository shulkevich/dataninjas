from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@once',
}

dag = DAG('stg_data_import', catchup=False, default_args=default_args)

data_import_task = BashOperator(
        task_id='data_import',
        bash_command="python3 /lessons/py/data_import.py",
        dag=dag
)

data_import_task
