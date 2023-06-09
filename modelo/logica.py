from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import torch

# Crear el objeto MinMaxScaler
scaler = MinMaxScaler()
Data=pd.read_csv("./modelo/Datos_Transformados.csv")
# Ajustar y transformar los datos
Data['Total stops'] = scaler.fit_transform(Data[['Total stops']])
Data['Departure_Day'] = scaler.fit_transform(Data[['Departure_Day']])
Data['Departure_Month'] = scaler.fit_transform(Data[['Departure_Month']])
Data['Departure_Year'] = scaler.fit_transform(Data[['Departure_Year']])
Data['Price'] = scaler.fit_transform(Data[['Price']])

model = torch.jit.load('./modelo/modelo_precios_boleto.pt')
model.eval()

# Ajustar y transformar los datos
def Normalizar(paradas,dia,mes,year):

    min_parada,max_parada=0,3
    day_min,day_max=1,31
    mount_min,mount_max=2,4
    year_min,year_max=2022.0,2022
    paradas=(paradas-min_parada)/(max_parada-min_parada)
    dia=(dia-day_min)/(day_max-day_min)
    mes=(mes-mount_min)/(mount_max-mount_min)
    try:
        year= (year-year_min)/(year_max-year_min)
    except:
        year=0


    return [paradas,dia,mes,year]

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
       lista_source[valor_source]=1
       lista_destino[valor_destino]=1
       return list(lista_aero)+list(lista_source)+list(lista_destino)

def Predic(aerolinea,source,Destino,escalas,fecha_day,fecha_mes,fecha_year):
    datos_1=preparacion_datos(aerolinea,source,Destino)
    datos_2=Normalizar(escalas,fecha_day,fecha_mes,fecha_year)
    lista=datos_1+datos_2
    lista_datos = [float(valor) for valor in lista]
    device = torch.device('cpu')
    S = torch.tensor(lista_datos, device=device)
    a=model(S).detach().numpy()
    return scaler.inverse_transform([a])[0][0]