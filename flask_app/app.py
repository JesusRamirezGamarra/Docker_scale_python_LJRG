import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    container_id = os.uname()[1]
    return f"hello world {container_id} --- LucioJesusRamirezGamarra"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)