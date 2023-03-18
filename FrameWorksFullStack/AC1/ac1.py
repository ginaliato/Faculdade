from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
  resultado = 'Digite as notas na URL'

  n1 = request.args.get('n1')
  n2 = request.args.get('n2')

  if n1 and n2:

    n1 = float(n1)
    n2 = float(n2)

    media = (n1 + n2) / 2
    resultado = (f"Primeira nota: <b>{n1}</b> <p> Segunda nota: <b> {n2} </b> </strong> <p> Media: <b> {media} </b>")

  return resultado


if __name__ == '__main__':
  app.run(debug=True)