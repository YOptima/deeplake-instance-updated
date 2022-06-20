import sys
import pandas as pd
import time

filename = sys.argv[1]
curr_date = time.strftime("%d%m%Y")
inputfile = filename + "_" + curr_date + ".csv"
df = pd.read_csv(inputfile, dtype='unicode', error_bad_lines=False)
df.drop(df.tail(7).index,inplace=True)
df.drop(['Impressions', 'Total Conversions', 'Clicks'], axis=1, inplace=True)
df.replace('Unknown', '', inplace = True)
df['Dimension_value'] = df[df.columns.values]
df = df['Dimension','Country','Dimension_value']
outputfile = filename + ".csv"
df.to_csv(outputfile, index = False)
