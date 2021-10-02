f = open('monedas.txt','w')
f.write('dolares,3,4')
f.close()

fr  = open('monedas.txt','r')
monedas = fr.read()
print(monedas)