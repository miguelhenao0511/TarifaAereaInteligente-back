import numpy as np
from datetime import datetime
from datetime import timedelta
from modelo.Prediccion import Predic

### puerto 5432

# Ajustar y transformar los datos
def Normalizar(paradas,dia,mes,year):

    min_parada,max_parada=0,3
    day_min,day_max=1,31
    mount_min,mount_max=2,4
    year_min,year_max=2022.0,2022
    #Normalizacion
    paradas=(paradas-min_parada)/(max_parada-min_parada)
    dia=(dia-day_min)/(day_max-day_min)
    mes=(mes-mount_min)/(mount_max-mount_min)
    try:
        year= (year-year_min)/(year_max-year_min)
    except:
        year=0
    return [paradas,dia,mes,year]

# se encarga de procesar los datos y generar un array normalizado
# para aerolinea,source,destino
def preparacion_datos(aerolinea,source,destino):
       aero="Air_"+aerolinea
       source="Source_"+source
       destino="Destination_"+destino
       aerolines={'Air_Aeroflot':0, 'Air_Air Canada':1, 'Air_Air France':2,
       'Air_American Airlines':3, 'Air_British Airways':4, 'Air_Delta':5,
       'Air_Emirates':6, 'Air_Finnair':7, 'Air_Finnair, American Airlines':8,
       'Air_KLM':9, 'Air_LOT':10, 'Air_Lufthansa':11, 'Air_Lufthansa, Egypt Air':12,
       'Air_Multiple Airlines':13, 'Air_Qatar Airways':14, 'Air_SAUDIA':15, 'Air_SWISS':16,
       'Air_TAP AIR PORTUGAL':17, 'Air_Turkish Airlines':18, 'Air_United Airlines':19}
       sources={'Source_NYC':0, 'Source_PAR':1, 'Source_RUH':2, 'Source_SVO':3}
       Destinos={'Destination_NYC':0, 'Destination_PAR':1, 'Destination_RUH':2,'Destination_SVO':3}
       valor_aero=aerolines[aero]
       valor_source=sources[source]
       valor_destino=Destinos[destino]
       lista_aero=np.zeros(20)
       lista_source=np.zeros(4)
       lista_destino=np.zeros(4)
       lista_aero[valor_aero] = 1
       lista_source[valor_source]= 1
       lista_destino[valor_destino]= 1
       return list(lista_aero)+list(lista_source)+list(lista_destino)

# genera un arrreglo con fechas a predecir
def Fecha(Fechas,cant_fechas):
    fecha = datetime.strptime(Fechas, "%Y-%m-%d")
    Fechas=[fecha+timedelta(days=i) for i in range(0,cant_fechas)]
    return Fechas

## Funcion a llamar
def Datos_Pronostico(aerolinea,source,Destino,escalas,fecha,cant_fechas):
     Datos_base=preparacion_datos(aerolinea,source,Destino)
     Dates=Fecha(fecha,cant_fechas)
     Datos_completos=[]
     for date in Dates:
          Datos_Normalizados=Normalizar(escalas,date.day,date.month,date.year)
          Datos_completos.append(Datos_base+Datos_Normalizados)
     return flatten(Predic(Datos_completos).tolist())

def flatten(array_list):
    return [element for sublist in array_list for element in sublist]