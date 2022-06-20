import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
num_of_column = df.shape[1]
df = df.dropna(thresh = int(num_of_column/2))
df['Advertiser ID'] = pd.to_numeric(df['Advertiser ID'],errors='coerce')
df = df.dropna(subset = ['Advertiser ID'])
df['Advertiser ID'] = df['Advertiser ID'].astype('int')
df.replace('Unknown', '', inplace = True)
df["Date"] = pd.to_datetime(df["Date"])
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False)

