import requests

url = 'http://localhost:5000/dados'
data = {
    'campo1': '1',
    'campo2': 'TESTANDO SE ESTA SALVANDO DADOS LALALALLALAL'
}
response = requests.post(url, json=data)