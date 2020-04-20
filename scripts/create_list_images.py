import os

l=os.listdir()
ls=[i for i in os.listdir() if i[-3:] in ["jpg","peg","png"]]

f=open('list.txt','w')
d=os.getcwd()+'/'
for i in ls:
    with open(i[:-3]+'txt','r') as t:
        if len(t.read()) < 2: continue
    f.write(d+i+'\n')

f.close()
    
