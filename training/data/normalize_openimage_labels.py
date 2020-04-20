import os
import re
from PIL import Image


files=[i for i in os.listdir() if i[-3:]=="txt"]

for f in files:

    fil = open(f,'r').readlines()
    
    with Image.open(f[:-3]+"jpg") as img:
        w,h = img.size
    data=""
    for x in fil:
        
        x = re.sub("(Bottle)|(Ball)|(Tin can)","3",x,flags=re.IGNORECASE)

        x = re.sub("(Handgun)|(Hair dryer)|(Computer Mouse)","4",x,flags=re.IGNORECASE)

        x = re.sub("(Hat)|(Ruler)|(Frying Pan)","0",x,flags=re.IGNORECASE)

        x = re.sub("(Pen)|(Screwdriver)|(Chopsticks)","2",x,flags=re.IGNORECASE)

        l = list(map(float,x.split()))
        
        l[0]=int(l[0])
        l[1],l[3]=l[1]/w,l[3]/w
        l[2],l[4]=l[2]/h,l[4]/h
        
        iw=l[3]-l[1]
        ih=l[4]-l[2]
        
        cenx=l[1]+(iw/2)
        ceny=l[2]+(ih/2)



        data+=' '.join([str(i) for i in [l[0],cenx,ceny,iw,ih]]) +'\n'
    
    with open(f,'w') as fnew:
        fnew.write(data)

