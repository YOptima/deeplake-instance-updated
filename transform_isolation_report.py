import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
n=int(sys.argv[2])
df.drop(df.tail(n).index,inplace=True)
df.replace('Unknown', '', inplace = True)
df["Date"] = pd.to_datetime(df["Date"])
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False)

