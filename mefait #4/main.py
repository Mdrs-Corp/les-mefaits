import os, json
import random
dos=lambda path: os.mkdir(path)
def file(path, content):
    f = open(path+".txt", "a")
    f.write(content)
    f.close()

with open('paths.json') as f:
  RJOHICQSBKJRHKUSHRJLIQZEROIHU = json.load(f)

a = random.randrange(10, 30)
b = random.randrange(10, 30)
nq = {"question": ("Sa fait combien"+str(a)+"*"+str(b)),
"anwsers": [str(i) for i in range(0, 1000)],
"correct": a*b}
RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"].append(nq)

nq = {"question": "POG⁈",
"anwsers": ["POG"+" "*i for i in range(0, 50)]+["pa POG"],
"correct": 50}
RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"].append(nq)

nq = {"question": "Hotel⁈",
"anwsers": ["Trivago"],
"correct": 0}
RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"].append(nq)

dos("./res")
path='./res/'
for KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ in RJOHICQSBKJRHKUSHRJLIQZEROIHU["questions"]:
    # La question en titre de fichier text
    dos(path+"["+KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["question"]+"]")
    file(path+"["+KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["question"]+"]"+"/C LA QUESTION PTN", "https://bit.ly/IqT6zt")

    OERIJZEOZRJIERZEORPJIKJOEIZR = KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["anwsers"][KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["correct"]]

    for i in KLEZRJLKHSDHJLKETRHGUERIEHIUEZKJERQ["anwsers"]:
        dos(path+i)
        if i != OERIJZEOZRJIERZEORPJIKJOEIZR:
            os.system('cp hom.lnk "'+os.path.join(path,i)+'/non.lnk"')

    # continuer à la prochaine descendance
    path+=OERIJZEOZRJIERZEORPJIKJOEIZR+"/"
file(path+"GG", "https://rarible.com/token/0xF6793dA657495ffeFF9Ee6350824910Abc21356C:78401752367104886489714714523507263898292811518299422941796928245418816438273?tab=details")
