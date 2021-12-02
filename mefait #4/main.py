import os,csv
dos=lambda path: os.mkdir(path)
file=lambda path : os.system(f'echo pas de solution ici >> "{path}.txt"')

def parcours():
    " Parcours des data, renvoie la liste "
    qandr=open('qandr.csv')
    ligne=qandr.readline()
    while ligne:
        yield ligne.split(sep=';')
        ligne=qandr.readline()[:-1]
    qandr.close()
    
dos("./res")
path='./res/'
for brain in parcours():
    # L'indice de la solution
    good=int(brain[-1])
    brain.pop()

    # La question en titre de fichier text
    file(path+brain[0])
    brain.pop(0)
    
    for ind,content in enumerate(brain):
        dos(path+content)
        if ind!=good:
            os.system('cp hom.lnk '+path+content+"/fin.lnk")
            # renvoyer vers le début si on se trompe,
            # la vraie solution finale sera aussi accesible
            # seulement par un fichier fin.lnk
    
    # continuer à la prochaine descendance
    path+=brain[good]+"/"
    
