import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")

#print(url.status_code)
if url.status_code == 200:
    html = BeautifulSoup(url.text,"html.parser")
    
    #ctl00_cphContent_rgTipoCambio_ctl00__0
    fw = open('monedas.txt','w')
    fw.close()
    for c in range(0,7):
        id_fila = "ctl00_cphContent_rgTipoCambio_ctl00__" + str(c)
        fila = html.find('tr',{'id':id_fila})
        moneda = fila.find('td',{'class':'APLI_fila3'})
        tipoCambioCompra = fila.find('td',{'class':'APLI_fila2'})
        tipoCambioVenta = fila.find('td',{'class':'APLI_fila2'}).find_next()
        
        f = open('monedas.txt','a')
        f.write(moneda.get_text() + ',' + tipoCambioCompra.get_text() + ',' + tipoCambioVenta.get_text() + '\n')
        f.close()
        print( moneda.get_text() + " | " + tipoCambioCompra.get_text() + " | " + tipoCambioVenta.get_text())
else:
    print("ERROR AL NAVEGAR EN LA PAGINA " + str(url.status_code))