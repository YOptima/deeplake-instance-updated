import dask.dataframe as dd
import sys
import time

begin = time.time()
filename = sys.argv[1]
inputfile = filename + ".csv"
ddf = dd.read_csv(inputfile,dtype='unicode',error_bad_lines=False)
ddf = ddf.dropna(thresh = 20)
ddf["Date"] = dd.to_datetime(ddf["Date"])
ddf = ddf.replace('Unknown', '')
ddf.to_csv(filename+"/*.csv",index = False)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
