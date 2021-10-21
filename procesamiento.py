import requests, json
import pandas as pd
import urllib

#se consume la primea API y se guardan los nombres en una lista
url = requests.get("https://rxnav.nlm.nih.gov/REST/allconcepts.json?tty=IN")
text = url.text

data = json.loads(url.content)

data = data['minConceptGroup']['minConcept']
lista=[]
for i in data:
  lista.append(i['name'])

### Se consume la segunda API
"""
correctos = []
listaf = []
for i in lista:
  url2 = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{i}/synonyms/json")
  if url2.status_code == 200:
    listaf.append(i)
    correctos.append(json.loads(url2.content))
"""
# --------------

# Debido al tiempo que se demora consumiendo la segunda API, se decide guardar los resultados (lista de nombres y sinónimos) en archivos de texto.
sin_txt = []
with open("sinonimos.txt","r") as archivo:
    for linea in archivo:
        sin_txt.append(eval(linea))



listaf_txt = []
with open("listaf.txt","r") as archivo:
    for linea in archivo:
        listaf_txt.append(linea.rstrip())