import math

print('branch: ')
yes0 = int(input('How many samples in the tree are yes?: '))
no0 = int(input('How many samples in the tree are no?: '))
total0 = yes0+no0

entropybefore = -(yes0/total0)*(math.log2(yes0/total0)) - ((no0/total0)*(math.log2(no0/total0)))


print("node 1:")
yes = int(input('What is the number of yes in the first node?: \n'))
no = int(input('what is the number of no?: \n'))
total = yes+no

print('node 2:')
yes2 = int(input('What is the number of yes in the second node?: \n'))
no2 = int(input('what is the number of no?: \n'))
total2 = yes2+no2

entropy1 = -(yes/total)*(math.log2(yes/total)) - ((no/total)*(math.log2(no/total)))

entropy2 = -(yes2/total2)*(math.log2(yes2/total2)) - ((no2/total2)*(math.log2(no2/total2)))

weight1 = total
weight2 = total2
entropyafter = (total/total0)*entropy1 + (total2/total0)*entropy2

ig = entropybefore - entropyafter

print('[+] Information gain on node: '+str(entropybefore-entropyafter))
