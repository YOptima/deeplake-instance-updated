import csv
import sys
import subprocess
from datetime import date, timedelta, datetime
import argparse
import pathlib

parser = argparse.ArgumentParser()

parser.add_argument('--table_name', required=True)
parser.add_argument('--report_id', nargs='+', required=True)

args = parser.parse_args()
table_name = args.table_name
report_list = args.report_id

lock = pathlib.Path("lock_" + table_name)
report_date = ''

if not lock.exists():
    for report_id in report_list:
        curr_date = date.today().strftime("%d%m%Y")
        filename = report_id + "_" + curr_date + ".csv"
        subprocess.call("sudo python3 export_api.py --query_id " + report_id, shell = True)
        with open(filename, 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if "Date Range:" in row:
                    report_date = row[1][-10:]

        yesterday = date.today() - timedelta(days = 1)
        day = yesterday.strftime("%Y/%m/%d")
        file = pathlib.Path("lock_" + report_id)

        if report_date == day and not file.exists():
            subprocess.call("sudo python3 transform_pixel.py " + report_id, shell = True)
            subprocess.call("sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows  _datalake_dev." + table_name + " " + report_id + ".csv", shell = True)
            with open('lock_' + report_id, 'w') as fp:
                pass

    flag = True

    for report_id in report_list:
        file = pathlib.Path("lock_" + report_id)
        if not file.exists():
            flag = False

    if flag:
        subprocess.call("sudo python3 pixel_lookback.py " + table_name, shell = True)
        with open('lock_' + table_name, 'w') as fp:
            pass
        subprocess.call("bq query --use_legacy_sql=false 'Delete from _datalake_dev.{} where true'".format(table_name), shell = True)
