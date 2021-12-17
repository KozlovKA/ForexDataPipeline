from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime, timedelta

default_args= {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}

with DAG("forex_data_pipeline",
start_date = datatime(2021, 1, 1),
schedule_interval ="@daily",
default_args=default_args,
catchup = False) as dag:

