import csv
import sys
import subprocess
from datetime import date, timedelta, datetime
import argparse
import pathlib
from google.cloud import bigquery


parser = argparse.ArgumentParser()

parser.add_argument('--table_name', required=True)
parser.add_argument('--report_id', nargs='+', required=True)
parser.add_argument('--start_date', required=True)
parser.add_argument('--end_date', required=True)

args = parser.parse_args()
table_name = args.table_name
report_list = args.report_id
start_date = args.start_date
end_date = args.end_date


for report_id in report_list:
    curr_date = date.today().strftime("%d%m%Y")
    filename = report_id + "_" + curr_date + ".csv"
    subprocess.call("sudo python3 export_api.py --query_id " + report_id, shell = True)
    subprocess.call("sudo python3 transform_youtube.py " + report_id, shell = True)
    subprocess.call("sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows  _dv3_youtube." + table_name + " " + report_id + ".csv", shell = True)


subprocess.call("sudo python3 youtube_lookback_manual.py " + table_name + " " + start_date + " " + end_date, shell = True)
subprocess.call("bq query --use_legacy_sql=false 'Delete from _dv3_youtube.{} where true'".format(table_name), shell = True)


start =  datetime.strptime(start_date, '%d-%m-%Y')
end =  datetime.strptime(end_date, '%d-%m-%Y')

client = bigquery.Client()

query = """
UPDATE `dv3_youtube.{}` a
SET a.Campaign_ID = b.Campaign_ID
FROM (select distinct Campaign_ID, Line_Item_ID  from `mapping.dv3_entity_mapping` ) b
WHERE 
    a.Line_Item_ID=b.Line_Item_ID AND
    a.date >= {} AND
    a.date <= {}
""".format(table_name,start,end)

query_job = client.query(query)
