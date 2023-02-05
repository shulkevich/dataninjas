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
insert into dds.events (
    event_timestamp, hour, event_type, prior_event_type, referer_url)
select
    event_timestamp,
    extract(hour from event_timestamp) as hour,
    event_type,
    lag(event_type) over (partition by user_custom_id order by event_timestamp) as prior_event_type,
    referer_url
from
    ods.events
where event_timestamp::DATE < 
    '{{ds}}'::DATE - interval 1 'day'
    """,
)


ods = PostgresOperator(
    task_id='ods_creation',
    dag=dag,
    postgres_conn_id='postgres_project', # надо добавить коннекшн в эирфлоу
    sql="""insert into ods.events (event_timestamp, user_custom_id, event_type, page_url)
select
    event_timestamp,
    user_custom_id,
    coalesce(
        substring(e.page_url_path from '\/(.*)_'),
        substring(e.page_url_path from '\/(.*)')
    ) as event_type,
    page_url
from
    staging.events e
where event_timestamp::DATE < 
'{{ds}}'::DATE - interval 1 'day'
    """,
)

dds >> ods 