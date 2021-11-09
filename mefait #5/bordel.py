from docx import Document
from docx.shared import RGBColor,Pt
import random

asci=" .:-=+*#%@"[::-1]
title=input("Image à transformer: ")
filemig=open(title,'rb')
mig=filemig.read()
filemig.close()

w=int.from_bytes(mig[18:22],byteorder='little')

mig=mig[54:]

document = Document()
p = document.add_paragraph('')
p.paragraph_format.line_spacing = 0.5


for i in range(len(mig)-3,0,-3):
    truc=(mig[i]+mig[i+1]+mig[i+2])//3
    run=p.add_run(asci[int(truc/255*(len(asci)-1))])
    font = run.font
    font.color.rgb = RGBColor(mig[i+2],mig[i+1],mig[i])
    font.size = Pt(5)
    font.name="Consolas"
    if i%w==0:
        p.add_run('\n')
        print(int(100-i/len(mig)*100),"%")


document.save(title[:-4]+'.docx')
print(f"Saved as {title[:-4]}.docx")
