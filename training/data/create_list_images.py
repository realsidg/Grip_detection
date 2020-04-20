import os

ls=[i for i in os.listdir() if i[-3:] in ["jpg","peg","png"]]

f=open('list.txt','w')
d=os.getcwd()+'/'
for i in ls:
    f.write(d+i+'\n')
f.close()
    
