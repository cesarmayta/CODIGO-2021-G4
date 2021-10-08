#PROGRAMA PARA CONVERTIR TIPOS DE CAMBIO DE MONEDAS
#DEFINIR VARIABLES
fr  = open('monedas.txt','r')
monedas = fr.read()

filasMonedas = monedas.splitlines()
#print(filasMonedas)
dicTiposCambio = {}
for filaMoneda in filasMonedas:
    #filaMoneda = 'Dolar de N.A.,4.127,4.134'
    registroMoneda = filaMoneda.split(',')
    #registroMoneda = ['Dolar de N.A','4.127','4.134']
    dicTiposCambio.update({
        registroMoneda[0]:float(registroMoneda[2])
    })

print(dicTiposCambio)
#DEFINICIÓN DE VALORES DE ENTRADA(INPUT)
print("=====================================")
print("       CONVERTIDOR DE MONEDAS        ")
print("=====================================")
monedaDestino = ""
while(monedaDestino != "salir"):
    monedaDestino = input("Ingrese moneda de destino(dolares,euros,peso mexicano,yen japones) : ")
    if(monedaDestino != "salir"):
        monedaOrigenMonto = float(input("Ingresa monto a convertir : "))
        #PROCESO O LOGICA DE NEGOCIO
        #VERSION 001 SOLUCIÓN
        tipoCambio = dicTiposCambio[monedaDestino]
            
        #CALCULAMOS EL MONTO DESTINO
        monedaDestinoMonto = monedaOrigenMonto / tipoCambio

        #MOSTRAR DATOS DE SALIDA
        strMontoResultado = "{:.2f}".format(monedaDestinoMonto)
        print("el monto en " + monedaDestino + " es " + strMontoResultado)
        
print("ADIOS !!!")

