import csv
import sys
import subprocess
from datetime import date, timedelta, datetime
import argparse
import pathlib

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
    subprocess.call("sudo python3 transform_pixel.py " + report_id, shell = True)
    subprocess.call("sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows  _datalake_dev." + table_name + " " + report_id + ".csv", shell = True)
    

subprocess.call("sudo python3 pixel_lookback_manual.py " + table_name + " " + start_date + " " + end_date, shell = True)
subprocess.call("bq query --use_legacy_sql=false 'Delete from _datalake_dev.{} where true'".format(table_name), shell = True)
