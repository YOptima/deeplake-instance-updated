import os
import sys
import pathlib
from datetime import date, timedelta, datetime
import subprocess


def main():
    report_id_channel = sys.argv[4]
    report_id_category = sys.argv[3]
    report_id_tod = sys.argv[1]
    report_id_tod_withttc = sys.argv[2]
    yesterday = date.today() - timedelta(days = 1)
    curr_date = yesterday.strftime("%Y/%m/%d")

    file = pathlib.Path("lock_isolation")
    file1 = pathlib.Path("lock_mapping")
    if curr_date == date_validator(report_id_channel, "13") and curr_date == date_validator(report_id_category,"16") and curr_date == date_validator(report_id_tod, "15") and curr_date == date_validator(report_id_tod_withttc, "16") and not file.exists() and file1.exists():
        with open("lock_isolation", "w") as fp:
            pass
        timestamp = datetime.now()
        print("Isolation tables data loading to bigquery Started at ", timestamp)
        subprocess.call("./gcs_isolation_transfer.sh " + report_id_tod + " 17 " + report_id_tod_withttc + " 17 " + report_id_category + " 17 " + report_id_channel + " 15", shell = True)
        timestamp = datetime.now()
        print("Isolation tables data loading to bigquery done at ", timestamp)

def date_validator(report_id, tail):
    curr_date = date.today().strftime("%d%m%Y")
    filename = report_id + "_" + curr_date + ".csv"
    cmd = 'tail -' + tail + " " + filename + ' | head -1 | tail -c 11'
    report_date = os.popen(cmd).read()
    return report_date.strip()


if __name__ == "__main__":
    main()
