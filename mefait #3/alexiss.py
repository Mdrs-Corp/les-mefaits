import os
import random
filemig=open('alexis en 116x116.bmp','rb')
derail=filemig.read()
filemig.close()
filedrail=open('alexis en 16x16.bmp','rb')
miniderail=filedrail.read()
filedrail.close()
a = 2

if not os.path.exists("./denis-saint-benois-de-moselle"):
  os.mkdir("./denis-saint-benois-de-moselle")

title=""
for i in range(10):title+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
rend=open('./denis-saint-benois-de-moselle/'+title+'title.bmp','ab')


entete=derail[:54]
derail=derail[54:]


def tocolored(coul:tuple,toma=miniderail):
    tabl=[]
    oww = int.from_bytes(toma[18:22], byteorder='little')
    toma=toma[54:]
    c = []
    for i in range(0,len(toma),3):
        truc=(toma[i]+toma[i+1]+toma[i+2])/(3*255)
        if i%(oww*3)==0 and i!=0:
            tabl.append(c)
            c = []
        c.append(bytes([int(truc*coul[0]), int(truc*coul[1]), int(truc*coul[2])]))
    tabl.append(c)
    return tabl


ow = int.from_bytes(entete[18:22], byteorder='little')
oh = int.from_bytes(entete[22:26], byteorder='little')
w = (ow*a)
h = (oh*a)
nw = w.to_bytes(4, byteorder="little")
nh = h.to_bytes(4, byteorder="little")


for i in range(54):
    if i>=18 and i<26:
        if i<22:
            rend.write(bytes([nw[i-18]]))
        else:
            rend.write(bytes([nh[i-22]]))
    else:
        rend.write(bytes([entete[i]]))



def getpixel(x, y):
    return derail[3*(x+y*ow)],derail[3*(x+y*ow)+1],derail[3*(x+y*ow)+2]


for i in range(h):
    for j in range(w):
        c=tocolored(getpixel(int(j/a), int(i/a)))
        rend.write(c[(i)%16][(j)%16])

rend.close()
