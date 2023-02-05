from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sql_dag_insert',
    default_args=args,
    description='Dag to create layers',
    schedule_interval='0 0 * * *',
)

dds = PostgresOperator(
    task_id='dds_creation',
    dag=dag,
    postgres_conn_id='postgres_project', # надо добавить коннекшн в эирфлоу
    sql="""
    select ...
    where event_timestamp::DATE < 
    '{{ds}}'::DATE - interval 1 'day'
    """,
)


ods = PostgresOperator(
    task_id='ods_creation',
    dag=dag,
    postgres_conn_id='postgres_project', # надо добавить коннекшн в эирфлоу
    sql="sql/staging_ods.sql",
)

mart = PostgresOperator(
    task_id='mart_creation',
    dag=dag,
    postgres_conn_id='postgres_project', # надо добавить коннекшн в эирфлоу
    sql="""
    select ...
    where event_timestamp::DATE 
    """,
)

dds >> ods >> mart
