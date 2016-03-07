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
node1 = str(df.iloc[0,0])
i = [1,0] # initialize column position
r = [1]
work = range(len(row1))
remain = len(row1)
for each in work:
   # get to this eventually