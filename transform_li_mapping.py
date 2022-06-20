import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
df = df.dropna(thresh = 8)
df.replace('Unknown', '', inplace = True)
df = df.drop(columns=['Impressions', 'Total Conversions', 'Clicks'])
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False)
