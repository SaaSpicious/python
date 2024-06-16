#!/usr/bin/python3

import random

length=18
astr="* "
for i in range(length):
    line=""
    for j in range(length-i):
        line+="  "
    line+=astr
    print (line)
    for i in range(4):
        if(random.randint(0,2)==0):
            astr+="*"
        elif(random.randint(0,2)==1):
            astr+="-"
        else:
            astr+=" "

for i in range(length+1):
    line=""
    for j in range(i):
        line+="  "
    line+=astr
    print (line)
    astr=astr[:len(astr)-4]

