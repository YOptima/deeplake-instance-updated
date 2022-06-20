from datetime import date, timedelta, datetime
import subprocess
import sys
from datetime import date, timedelta, datetime

table_name = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]

start_date =  datetime.strptime(start.strip(), '%d-%m-%Y')
end_date =  datetime.strptime(end.strip(), '%d-%m-%Y')

while start_date <= end_date:
    curr_date = start_date.strftime("%Y%m%d")
    subprocess.call('sudo bq cp -f _dv3_youtube."{}"$"{}" dv3_youtube."{}"$"{}" '.format(table_name,curr_date,table_name,curr_date), shell = True)
    start_date = start_date + timedelta(days = 1)
