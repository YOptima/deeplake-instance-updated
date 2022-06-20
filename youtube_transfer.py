import subprocess

subprocess.call("sudo python3 youtube_reports.py --table_name ad --report_id 844266801 844265987 844265933 871848727 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name agip --report_id 760785536 760378817 844090624 871848185 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name category --report_id 847752317 847752983 847753257 871848368 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name city --report_id 847746906 847748355 847749920 871848729 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name conversion --report_id 760389608 760392596 844090903 871848187 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name device_type --report_id 760378117 760775337 844090623 871848366 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name interest --report_id 760548300 760545236 844090904 871848367 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name placement --report_id 760549131 906764877 847755922 871848730 ", shell = True)
subprocess.call("sudo python3 youtube_reports.py --table_name video --report_id 847744518 847744517 847744520 871848728 ", shell = True)
subprocess.call("./instance_stop.sh", shell = True)
