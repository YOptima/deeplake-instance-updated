import fileinput

file = open('pixel_transfer_temp.py', 'r')
replacement = ""
for line in file:
    if "ad" in line or "agip" in line or "category" in line or "city" in line or "conversion" in line or "device_type" in line or "interest" in line or "placement" in line or "video" in line:
        content = line.split(' ')
        content.insert(6,'2342424242432')
        new_line = " ".join(str(x) for x in content)
        replacement = replacement + new_line + "\n"
        #content = line.split(' ')
        #content.insert(6,'2342424242432')
    else:
        replacement = replacement + line + "\n"

file.close()

fout = open('pixel_transfer_temp.py', 'w')
fout.write(replacement)
fout.close()
