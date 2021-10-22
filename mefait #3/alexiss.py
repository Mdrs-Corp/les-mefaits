import random
filemig=open('alexis en 116x116.bmp','rb')
derail=filemig.read()
filemig.close()
filedrail=open('alexis en 16x16.bmp','rb')
miniderail=filedrail.read()
filedrail.close()
a = 2

title=""
for i in range(10):title+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
rend=open('./essais/'+title+'title.bmp','ab')


entete=derail[:54]
derail=derail[54:]


def tobyte(nb:int):
    he=hex(nb)[2:]
    while len(he)<2:
        he="0"+he
    return bytes.fromhex(he)

def tocolored(coul:tuple,toma=miniderail):
    tabl=[[]]
    ow = int.from_bytes(toma[18:22], byteorder='little')
    toma=toma[54:]
    for i in range(0,len(toma),3):
        truc=(toma[i]+toma[i+1]+toma[i+2])/(3*255)
        for couluer in coul[::-1]:
            tabl[-1].append(tobyte(int(truc*couluer)))
        if i%16==0 and i!=0:
            tabl.append([])
    return tabl
            

ow = int.from_bytes(entete[18:22], byteorder='little')
oh = int.from_bytes(entete[22:26], byteorder='little')
w = (ow*a)
h = (oh*a)
nw = w.to_bytes(4, byteorder="little")
nh = h.to_bytes(4, byteorder="little")


"""for i in range(54):
    if i>=18 and i<26:
        if i<22:
            rend.write(bytes([nw[i-18]]))
        else:
            rend.write(bytes([nh[i-22]]))
    else:
        rend.write(bytes([entete[i]]))"""



def getpixel(x, y):
    return derail[3*(x+y*ow)],derail[3*(x+y*ow)+1],derail[3*(x+y*ow)+2]


"""for i in range(h):
    for j in range(w):
        c=tocolored(getpixel(int(j/a), int(i/a)))
        rend.write(bytes(getpixel(int(j/a), int(i/a))))"""

rend.close()
