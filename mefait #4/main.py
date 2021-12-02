import os,csv
dos=lambda path: os.mkdir(path)
file=lambda path : os.system(f'echo pas de solution ici >> "{path}.txt"')

def parcours():
    qandr=open('qandr.csv')
    ligne=qandr.readline()
    while ligne:
        yield ligne.split(sep=';')
        ligne=qandr.readline()[:-1]
    qandr.close()
dos("./res")
path='./res/'
for brain in parcours():
    good=int(brain[-1])
    brain.pop()
    if file(path+brain[0]):
        print(brain)
    brain.pop(0)
    for content in brain:
        dos(path+content)
    path+=brain[good]+"/"
    
