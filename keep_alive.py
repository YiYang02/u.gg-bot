from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "I am sending a message so I don't sleep."

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()