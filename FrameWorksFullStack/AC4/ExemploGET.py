import requests

url = 'http://localhost:5000/dados'  

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro na requisição:', response.status_code)