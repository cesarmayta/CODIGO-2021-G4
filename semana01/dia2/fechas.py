import datetime

def ConvertirFechaEnDias(strFecha):
    resultado = (datetime.datetime.now() - datetime.datetime.fromisoformat(strFecha)).days
    return resultado 
    
print(ConvertirFechaEnDias("2000-01-01"))
print(ConvertirFechaEnDias("1980-01-01"))