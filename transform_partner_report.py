import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
df = df.dropna(thresh = 4)
df['Partner ID'] = pd.to_numeric(df['Partner ID'],errors='coerce')
df = df.dropna(subset = ['Partner ID'])
df['Partner ID'] = df['Partner ID'].astype('int')
df.drop(['Partner','Impressions', 'Total Conversions', 'Clicks'], axis=1, inplace=True)
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False,header = False)
