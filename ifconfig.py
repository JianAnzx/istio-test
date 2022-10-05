from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get("http://ifconfig.me/ip")
    return f"Your web public IP address is {r.text}"

@app.route('/status<code>')
def status(code):
    print("debug" + code)
    if(100 < int(code) <= 530):
        r = requests.get(f"http://httpstat.us/{code}")
        return f"Status code is {r.status_code}"
    else:
        return "Unknow status"

app.run(host='0.0.0.0', port=5000)

