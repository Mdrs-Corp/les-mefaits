import os, json
import random
dos=lambda path: os.mkdir(path)
def file(path):
    f = open(path+".txt", "a")
    f.write("https://bit.ly/IqT6zt")
    f.close()

with open('paths.json') as f:
  RJOHICQSBKJRHKUSHRJLIQZEROIHU = json.load(f)

a = random.randrange(10, 30)
b = random.randrange(10, 30)
nq = {"question": ("Sa fait combien"+str(a)+"*"+str(b)),
"anwsers": [str(i) for i in range(0, 1000)],
"correct": a*b}
RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"].append(nq)

nq = {"question": "Amato⁈",
"anwsers": ["Amato"+" "*i for i in range(0, 50)]+["pa Amato"],
"correct": 50}
RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"].append(nq)

dos("./res")
path='./res/'
for KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ in RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"]:
    # La question en titre de fichier text
    file(path+KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["question"])

    OERIJZEOZRJIERZEORPJIKJOEIZR = KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["anwsers"][KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["correct"]]

    for i in KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["anwsers"]:
        dos(path+i)
        if i != OERIJZEOZRJIERZEORPJIKJOEIZR:
            os.system('cp hom.lnk "'+os.path.join(path,i)+'/fin.lnk"')

    # continuer à la prochaine descendance
    path+=OERIJZEOZRJIERZEORPJIKJOEIZR+"/"
