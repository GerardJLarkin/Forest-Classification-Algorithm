import math
import pandas

def ig():
    print('branch: ')
    yes0 = int(input('How many samples in the tree are yes?: '))
    no0 = int(input('How many samples in the tree are no?: '))
    total0 = yes0+no0
    entropybefore = -(yes0/total0)*(math.log2(yes0/total0)) - ((no0/total0)*(math.log2(no0/total0)))
    print("node 1:")
    yes1 = int(input('What is the number of yes in the first node?: \n'))
    no1 = int(input('what is the number of no?: \n'))
    total = yes1+no1
    print('node 2:')
    yes2 = int(input('What is the number of yes in the second node?: \n'))
    no2 = int(input('what is the number of no?: \n'))
    total2 = yes2+no2
    entropy1 = -(yes1/total)*(math.log2(yes1/total)) - ((no1/total)*(math.log2(no1/total)))
    entropy2 = -(yes2/total2)*(math.log2(yes2/total2)) - ((no2/total2)*(math.log2(no2/total2)))
    entropyafter = (total/total0)*entropy1 + (total2/total0)*entropy2
    ig = entropybefore - entropyafter
    print('[+] Information gain on node: '+str(ig))

def read_data(csv):
    attr = ['True','False','mild','hot','cool','normal','high','rainy','sunny','overcast']
    playtennis = ['yes', 'no']
    data = pandas.read_csv(csv, header=0)
    df = pandas.DataFrame(data)       
    print(df)
    header = df.columns.values.tolist()
    print('header: '+str(header[:4]))
    return df,playtennis,attr,header
    quantify_data(attr,playtennis,header,df)
        
ig()