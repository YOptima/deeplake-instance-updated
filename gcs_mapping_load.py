import os
import sys
import pathlib
from datetime import date, timedelta, datetime
import subprocess


def main():
    report_id_app = sys.argv[1]
    report_id_city = sys.argv[2]
    report_id_creative = sys.argv[3]
    report_id_isp = sys.argv[4]
    report_id_exchange = sys.argv[5]
    report_id_entity = sys.argv[6]
    report_id_li = sys.argv[7]
    yesterday = date.today() - timedelta(days = 1)
    curr_date = yesterday.strftime("%Y/%m/%d")

    file = pathlib.Path("lock_mapping")
    if curr_date == date_validator(report_id_app, "6") and curr_date == date_validator(report_id_city, "11") and curr_date == date_validator(report_id_creative, "9") and curr_date == date_validator(report_id_isp, "6") and curr_date == date_validator(report_id_exchange, "10") and curr_date == date_validator(report_id_entity, "17") and curr_date == date_validator(report_id_li, "12") and not file.exists():
        with open("lock_mapping", "w") as fp:
            pass
        timestamp = datetime.now()
        print("Mapping table data loading to bigquery Started at ", timestamp)
        subprocess.call("./gcs_mapping_transfer.sh " + report_id_app + " 8 " + report_id_city + " 13 " + report_id_creative + " 11 " + report_id_isp + " 8 " + report_id_exchange + " 12 " + report_id_entity + " 19 " + report_id_li, shell = True)
        timestamp = datetime.now()
        print("Mapping table data loading to bigquery ended at ", timestamp)
    elif file.exists() and curr_date != date_validator(report_id_app, "6"):
        os.remove("lock_mapping")


def date_validator(report_id, tail):
    curr_date = date.today().strftime("%d%m%Y")
    filename = report_id + "_" + curr_date + ".csv"
    cmd = 'tail -' + tail + ' ' + filename + ' | head -1 | tail -c 11'
    report_date = os.popen(cmd).read()
    return report_date.strip()


if __name__ == "__main__":
    main()
