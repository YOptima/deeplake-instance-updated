import os
import sys
import pathlib
from datetime import date, timedelta, datetime
import subprocess


def main():
    report_id_main = sys.argv[1]
    report_id_ttc = sys.argv[2]
    report_id_advertiser = sys.argv[3]
    report_id_validation = sys.argv[4]
    yesterday = date.today() - timedelta(days = 1)
    curr_date = yesterday.strftime("%Y/%m/%d")
    file = pathlib.Path("lock")
    if curr_date == date_validator(report_id_main, "27") and curr_date == date_validator(report_id_ttc, "28") and curr_date == date_validator(report_id_advertiser, "8") and curr_date == date_validator(report_id_validation, "7") and not file.exists():
        with open("lock", "w") as fp:
            pass
        timestamp = datetime.now()
        print("Main table data loading to bigquery Started at ", timestamp)
        subprocess.call("./gcs_main_transfer.sh " + report_id_main + " " + report_id_ttc, shell = True)
        timestamp = datetime.now()
        print("Main table data loading to bigquery done at ", timestamp)


def date_validator(report_id, tail):
    curr_date = date.today().strftime("%d%m%Y")
    filename = report_id + "_" + curr_date + ".csv"
    cmd = 'tail -' + tail + " " + filename + ' | head -1 | tail -c 11'
    report_date = os.popen(cmd).read()
    return report_date.strip()


if __name__ == "__main__":
    main()
