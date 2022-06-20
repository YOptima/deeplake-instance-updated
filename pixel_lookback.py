from datetime import date, timedelta, datetime
import subprocess
import sys

table_name = sys.argv[1]

for i in range(1,8):
    yesterday = date.today() - timedelta(days = i)
    curr_date = yesterday.strftime("%Y%m%d")
    subprocess.call('sudo bq cp -f _datalake_dev."{}"$"{}" datalake."{}"$"{}" '.format(table_name,curr_date,table_name,curr_date), shell = True)
