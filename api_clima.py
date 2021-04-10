#Nome da cidade: Osasco, SP
#WOEID: 455894

#https://api.hgbrasil.com/weather?woeid=455894

#{"by":"woeid","valid_key":false,"results":{"temp":18,"date":"08/04/2021","time":"23:28","condition_code":"27","description":"Tempo limpo","currently":"noite","cid":"","city":"Osasco, SP","img_id":"27n","humidity":82,"wind_speedy":"3.6 km/h","sunrise":"06:17 am","sunset":"05:59 pm","condition_slug":"clear_night","city_name":"Osasco","forecast":[{"date":"08/04","weekday":"Qui","max":25,"min":15,"description":"Ensolarado","condition":"clear_day"},{"date":"09/04","weekday":"Sex","max":26,"min":13,"description":"Ensolarado","condition":"clear_day"},{"date":"10/04","weekday":"Sáb","max":27,"min":15,"description":"Ensolarado","condition":"clear_day"},{"date":"11/04","weekday":"Dom","max":28,"min":15,"description":"Ensolarado","condition":"clear_day"},{"date":"12/04","weekday":"Seg","max":27,"min":15,"description":"Parcialmente nublado","condition":"cloudly_day"},{"date":"13/04","weekday":"Ter","max":20,"min":16,"description":"Trovoadas dispersas","condition":"storm"},{"date":"14/04","weekday":"Qua","max":22,"min":15,"description":"Parcialmente nublado","condition":"cloudly_day"},{"date":"15/04","weekday":"Qui","max":21,"min":15,"description":"Alguns chuviscos","condition":"rain"},{"date":"16/04","weekday":"Sex","max":20,"min":16,"description":"Tempestades isoladas","condition":"storm"},{"date":"17/04","weekday":"Sáb","max":24,"min":15,"description":"Tempo nublado","condition":"cloud"}]},"execution_time":0.1,"from_cache":false}

import requests 
import json

req = None

cidade ='455894'
link = 'https://api.hgbrasil.com/weather?woeid='+cidade


try:
    print(f'Buscando de: {link}')
    req = requests.get(link)
    print(req)
    texto = req.text
    result = dict(json.loads(texto))
    result = result['results']
    
    forecast = result['forecast']
    
    max = forecast[0]['max']
    min = forecast[0]['min']
    
    temp = result['temp']
    print(f'Temperatura {temp}c maxima {max}c minima {min}c')
    
    dia = f'No dia{result["date"]}'
    print(dia)
    
    
except Exception as er:
    print(f'Tem porra nenhuma aqui em {cidade}: {er}')
    print(req)