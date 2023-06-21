from sklearn.preprocessing import MinMaxScaler
import pandas as pd
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

# esta funicon resive los datos normalizados y realiza la preccion
# retorna un array con los resultados
def Predic(lista_datos):
    lista_datos = [[float(valor) for valor in fila] for fila in lista_datos]
    device = torch.device('cpu')
    S = torch.tensor(lista_datos, device=device)
    list_predic=model(S).detach().numpy()

    return scaler.inverse_transform(list_predic)