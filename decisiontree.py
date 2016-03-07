import pandas as pd
import time
from operator import add

name = input("What is the filename? \n")
print('\nReading from '+name)
time.sleep(1)
csv = pd.read_csv(name)
df = pd.DataFrame(data=csv)
numcol = len(csv.columns)
print('\n[+] '+str(numcol)+' classifications found.')
time.sleep(1)
row1 = pd.read_csv(name, usecols=[0])
print('\n[~] Running entropy analysis on each node...')
time.sleep(1)
print(df.columns)
col00 = str(df.iloc[0,0])
i = [1,0] # initialize column position
r = [1]
work = range(len(row1))
for each in work:
    if str(df.iloc[i]) == col00:
        map(add, i, r)
        remain = len(row1) - 1
    elif str(df.iloc[i]) != col00:
        map(add,i,r)
        col10=str(df.iloc[1,0])
        remain = len(row1) - 1
        print('\n [+] Found child node... '+str(remain)+' checks left.')
