import sys
import pandas as pd
import time
import subprocess
from datetime import date, timedelta, datetime
import pathlib
import csv


filename = sys.argv[1]
report_id = filename
table_name = 'currency_conversion'
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
lock = pathlib.Path("lock_" + report_id)

if not lock.exists():
    subprocess.call("sudo python3 export_api.py --query_id " + report_id, shell = True)
    with open(inputfile, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if "Date Range:" in row:
                report_date = row[1][-10:]
        yesterday = date.today() - timedelta(days = 1)
        day = yesterday.strftime("%Y/%m/%d")
        if report_date == day:
            df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
            df = df.dropna(thresh = 4)
            df['currency'] = 'USD'
            df['Total Media Cost (USD)'] = df['Total Media Cost (USD)'].astype('float')
            df['Total Media Cost (Advertiser Currency)'] = df['Total Media Cost (Advertiser Currency)'].astype('float')
            df['conv'] = df['Total Media Cost (USD)']/df['Total Media Cost (Advertiser Currency)']
            df.drop(['Advertiser Currency','Total Media Cost (USD)','Total Media Cost (Advertiser Currency)'], axis=1, inplace=True)
            df["Date"] = pd.to_datetime(df["Date"])
            outputfile = filename + ".csv"
            df.to_csv(outputfile, index = False)
            subprocess.call("sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows  deepm." + table_name + " " + report_id + ".csv", shell = True)
            with open('lock_' + report_id, 'w') as fp:
                pass
