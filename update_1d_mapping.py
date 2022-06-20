import sys
import pandas as pd
import time

input = sys.argv[1] + '.csv'
df = pd.read_csv(input, dtype='unicode', error_bad_lines=False)
df.insert(0,'Dimension',sys.argv[1])
#df = df['Dimension','Country','Dimension_value']
output = sys.argv[1] + '_1d.csv'
df.to_csv(output, index = False)
