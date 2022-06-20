import pathlib
import subprocess

file1 = pathlib.Path("lock_ad")
file2 = pathlib.Path("lock_agip")
file3 = pathlib.Path("lock_city")
file4 = pathlib.Path("lock_category")
file5 = pathlib.Path("lock_conversion")
file6 = pathlib.Path("lock_device_type")
file7 = pathlib.Path("lock_interest")
file8 = pathlib.Path("lock_placement")
file9 = pathlib.Path("lock_video")

if file1.exists() and file2.exists() and file3.exists() and file4.exists() and file5.exists() and file6.exists() and file7.exists() and file8.exists() and file9.exists():
    subprocess.call("sudo gsutil cp lock_ad gs://trigger-youtube", shell = True)
