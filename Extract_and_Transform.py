import requests
import json
import time
from tinydb import TinyDB, database, Query



i = 1
isEmpty = False
listaFinal = []
while isEmpty == False: #mantem o loop enquanto o array nao retornar vazio
  url = f"http://challenge.dienekes.com.br/api/numbers?page={i}"

  payload={}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  json_data = json.loads(response.text)
  try:
    listaTemporaria = json_data['numbers']
  except:
    '''
    Em tempo de execução, devido a velocidade algumas requisições falham
    caso falhe, o código espera dois segundos e tenta novamente
    o problema nao ocorreu novamente após isso
    '''
    time.sleep(2.0)
    url = f"http://challenge.dienekes.com.br/api/numbers?page={i}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    listaTemporaria = json_data['numbers']

  if not listaTemporaria: # verifica se o array esta vazio
    isEmpty = True
  else:
    listaFinal.extend(listaTemporaria) # faz o append da lista atual na lista definitiva
    i +=1

 ### Inicio da fase 2 - Ordenação
 # Lógica utilizada : Ordenação Bubble Sort
 # Apesar da baixa perfomance, ele é mais eficiente em vetores pré-ordenados  

size = len(listaFinal) # persiste o tamanho da lista
sizeMinusOne = size-1 # persiste o tamanho da lista menos um
for i in range(sizeMinusOne): # função range itera apartir do 0 por isso usamos sizeMinusOne

    for j in range(sizeMinusOne-i): 
        if listaFinal[j] > listaFinal[j + 1] : #verifica se cada posição é maior que a posição seguinte
            listaFinal[j], listaFinal[j + 1] = listaFinal[j + 1], listaFinal[j] #caso seja, inverte a posição dos elementosZ

database = TinyDB(r'C:\Users\Public\database.json')
database.insert({'Lista': listaFinal}) # salva lista ordenada em uma base local, para que possa ser acessada e retornada pela api

            
