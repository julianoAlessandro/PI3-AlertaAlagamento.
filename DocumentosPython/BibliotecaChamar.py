#Versão:Python 3.12.0
#Autor:Juliano Alessandro dos Santos
#Dia: 31/10/2023
#Biblioteca: Requests utilizada para fazer a requisição de um serviço na Web
def BuscarPrecipitacao(latitude,longitude):
    import requests as r
    url = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.0&query={latitude},{longitude}&subscription-key=g9cogBIB7upc32WNQMsBt-fsO5z2jpNurTF-r3mwVLQ'
    valores = r.get(url)
    formatoDicionario = valores.json()
    resumoPrecipitação = formatoDicionario['results'][0]['precipitationSummary']
    print(resumoPrecipitação)
