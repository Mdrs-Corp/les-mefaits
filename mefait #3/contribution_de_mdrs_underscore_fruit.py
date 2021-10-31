f = open('alexis en 116x116.bmp', 'rb')
derail = f.read()
f.close()
f = open('alexis en 16x16.bmp', 'rb')
mini_derail = f.read()
f.close()

entete = derail[:54]
derail = derail[54:]
mini_derail = mini_derail[54:]

output = open('./essais/output.bmp', 'wb')
output.write(entete[:18])
output.write((116*16).to_bytes(4, 'little'))
output.write((116*16).to_bytes(4, 'little'))
output.write(entete[26:])

for y in range(0, 116*3, 3):
    for i in range(0, 16*3, 3):
        for x in range(0, 116*3, 3):
            c = (derail[x + y*116], derail[x+1 + y*116], derail[x+2 + y*116]) # couleur
            o = mini_derail[i*16 : (i+3)*16]
            for j in range(0, 16*3, 3):
                a = (o[j] + o[j+1] + o[j+2])/(255*3)

                b = int(a*c[0])
                g = int(a*c[1])
                r = int(a*c[2])
                output.write(b.to_bytes(1, 'little'))
                output.write(g.to_bytes(1, 'little'))
                output.write(r.to_bytes(1, 'little'))

output.close()