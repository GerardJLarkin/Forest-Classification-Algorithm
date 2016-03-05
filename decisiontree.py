import pandas as pd
import time

name = input("What is the filename? \n")
header = pd.read_csv(name)
numcol = len(header.columns)
print('\n'+str(numcol)+' nodes.'+'\n')
col = pd.read_csv(name, usecols=[0])
print('\n[+] Running entropy analysis on each node...')
time.sleep(1)