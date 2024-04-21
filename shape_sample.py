#!/usr/bin/python3

length=40
astr="*"
for i in range(length):
    line=""
    for j in range(length-i):
        line+=" "
    line+=astr
    print (line)
    astr+="**"

for i in range(length+1):
    line=""
    for j in range(i):
        line+=" "
    line+=astr
    print (line)
    astr=astr[:len(astr)-2]

