import create_dv3_report as config
import os
from pathlib import Path

with open('partner_list.csv', 'r') as t1, open('860199866.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

for line in filetwo:
    if line not in fileone:
        dict = {"youtube_ad.json":"ad", "youtube_agip.json":"agip", "youtube_category.json":"category", "youtube_city.json":"city", "youtube_conversion.json":"conversion", "youtube_device_type.json":"device_type", "youtube_interest.json":"interest", "youtube_placement.json":"placement", "youtube_video.json":"video"}
        replacement = "import subprocess \n"
        for key, value in dict.items():
            f = open('youtube_transfer.py', 'r')
            report = config.update_json(line.rstrip(),"config/youtube/" + key)
            for command in f:
                if value in command:
                    content = command.split(' ')
                    content.insert(6,report)
                    new_line = " ".join(str(x) for x in content)
                    replacement = replacement + new_line + "\n"
            f.close()
        replacement = replacement + "subprocess.call(\"./instance_stop.sh\", shell = True)" + "\n"
        fout = open('youtube_transfer_temp.py', 'w')
        fout.write(replacement)
        fout.close()

        dict = {"pixel.json":"dv3_pixelload_table", "pixel_withorder.json":"dv3_pixelload_withorderid_table"}
        replacement = "import subprocess \n"
        for key, value in dict.items():
            f = open('pixel_transfer.py', 'r')
            report = config.update_json(line.rstrip(),"config/pixel/" + key)
            for command in f:
                if value in command:
                    content = command.split(' ')
                    content.insert(6,report)
                    new_line = " ".join(str(x) for x in content)
                    replacement = replacement + new_line + "\n"
            f.close()
        replacement = replacement + "subprocess.call(\"./instance_stop.sh\", shell = True)" + "\n"
        fout = open('pixel_transfer_temp.py', 'w')
        fout.write(replacement)
        fout.close()
