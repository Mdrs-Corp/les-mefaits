import os
import random
bible=open('!THE HOLY BIBLE.txt','rb')
t=bible.read()
bible.close()
verses=t.split(b'\r\n\r\n')
mathieu='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, '
def convert(v:bytes):
    '''convertit et donne fichier like text'''
    v=str(v)
    rend=''
    for char in v:
        if char in mathieu:
            rend+=char
    return rend[2:]

def create(nb):
    for _ in range(nb):
        title=convert(random.choice(verses))
        while len(title)>252:
            title=convert(random.choice(verses))
        file=open("./denis-saint-benois-de-moselle/"+title+".txt","w")
        file.write("Alexis derail préfère la NSI à la SI")
        file.close()

if not os.path.exists("./denis-saint-benois-de-moselle"):
  os.mkdir("./denis-saint-benois-de-moselle")

create(50)