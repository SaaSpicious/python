#!/usr/bin/python3
max_number=100;
liner=0;
lines="";
totalcount=0;
prime=False;
for i in range(2,max_number):
    
    prime=False;
    for j in range(2,i//2+1):
        if i%j == 0:
            prime=True;
    if not prime:
        lines=lines+str(i)+", ";
        totalcount+=1
        if liner < 18:
            liner+=1;
        else:
            print(lines);
            liner=0;
            lines="";
print(lines);
print("found a total of "+str(totalcount)+" prime numbers!");