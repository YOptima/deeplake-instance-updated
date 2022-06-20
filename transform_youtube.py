import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
num_of_column = df.shape[1]
df = df.dropna(thresh = int(num_of_column/2))
df['YouTube Ad Group ID'] = pd.to_numeric(df['YouTube Ad Group ID'],errors='coerce')
df = df.dropna(subset = ['YouTube Ad Group ID'])
df['YouTube Ad Group ID'] = df['YouTube Ad Group ID'].astype('int')
df.replace('Unknown', '', inplace = True)
df["Date"] = pd.to_datetime(df["Date"])
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False)

