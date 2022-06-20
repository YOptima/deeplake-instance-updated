import pandas as pd
import time

curr_date = time.strftime("%d%m%Y")
inputfile = "734229253_" + curr_date + ".csv"
df=pd.read_csv(inputfile,dtype='unicode')
df.drop(df.tail(10).index,inplace = True)
keep_col = ['Line Item ID','Advertiser ID','Campaign ID','Insertion Order ID']
new_df = df[keep_col]
new_df.to_csv("734229253.csv", index=False)
