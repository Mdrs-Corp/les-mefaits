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
        file=open(title+".txt","w")
        file.write("Alexis derail préfère la NSI à la SI")
        file.close()
