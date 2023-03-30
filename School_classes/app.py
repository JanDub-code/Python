from flask import Flask
import requests

app = Flask(__name__)

req = requests.get('https://api.chucknorris.io/jokes/random')
req = req.json()
vtip = req['value']

kategorie = requests.get('https://api.chucknorris.io/jokes/random?category={category}')
kategorie = kategorie.json()
print(kategorie)

@app.route('/vtipecek')
def vtipecek():
    return f"<p> {vtip} </p>"

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

