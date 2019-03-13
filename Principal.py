import requests

NomeLista = []
NomeLista +=['https://www.google.com']
for i in NomeLista:
  response = requests.get(i).text
  print(response)
