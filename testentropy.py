# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:13:28 2016

@author: Dylan
"""

import math

yes = int(input('What is the number of yes?: \n'))
no = int(input('what is the number of no?: \n'))

entropy = -(yes/(yes+no))*math.log1p(2)*(yes/(yes+no))*-(no/(yes+no))*math.log1p(2)*(no/(yes+no)) //http://i.imgur.com/xVNo9ZE.png

print('[+] Entropy on sample node: '+str(math.fabs(entropy)))10