import subprocess

subprocess.call("sudo python3 pixel_reports.py --table_name dv3_pixelload_table --report_id 844266041 848930079 848929978 871848781 ", shell = True)
subprocess.call("sudo python3 pixel_reports.py --table_name dv3_pixelload_withorderid_table --report_id 743089227 844266034 848611470 871849516 ", shell = True)
subprocess.call("./instance_stop.sh", shell = True)
