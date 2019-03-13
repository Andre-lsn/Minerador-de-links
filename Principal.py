import requests

NomeLista = []
NomeLista +=['Https://google.com']
for i in Lista: 
  response = requests.get(i).text
  print(response)
  
