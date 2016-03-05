import pandas as pd
import time

name = input("What is the filename? \n")
print('\nReading from '+name)
time.sleep(1)
header = pd.read_csv(name)
numcol = len(header.columns)
print('\n[+] '+str(numcol)+' nodes.')
time.sleep(1)
col = pd.read_csv(name, usecols=[0])
print('\n[~] Running entropy analysis on each node...')
time.sleep(1)