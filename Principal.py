import requests

lsSites = ['https://www.google.com']
lsHistory = [lsSites[0]]

while len(lsSites) > 0:
  response = requests.get(lsSites.pop()).text
  
  temp = response.split("href=")
  lsLinks = []
  for i in temp:
    lineLink = i.split("\"")
    if len(lineLink) > 1:
      if "http" in lineLink[1] and not(lineLink[1] in lsHistory):     
        arquivo = open('lsHistory.txt','a')
        arquivo.write(lineLink[1])
        arquivo.close()
        lsSites += [lineLink[1]]
        lsHistory += [lineLink[1]]
        print(lineLink[1])

print(lsSites)
