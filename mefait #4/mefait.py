import os

if not os.path.exists(os.path.join(os.getcwd(),"denis-saint-benois-de-moselle")):
  os.mkdir(os.path.join(os.getcwd(),"denis-saint-benois-de-moselle"))


folders = [os.path.join(os.getcwd(),"denis-saint-benois-de-moselle")]


for i in range(5):
    nfolders = []
    for file in folders:
        npath = os.path.join(file, "nsi")
        os.mkdir(npath)
        nfolders.append(npath)
        npath = os.path.join(file, "si")
        os.mkdir(npath)
        nfolders.append(npath)
        f = open(os.path.join(file, "lequelle est le mieux.txt"), "w")
        f.write("(nsi)")
        f.close()
    folders = nfolders
