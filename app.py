from flask import Flask
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import os

app = Flask(__name__)


@app.route('/')
def index():
    resp = urlopen('http://api.bestchange.ru/info.zip')
    zipFile = ZipFile(BytesIO(resp.read()))
    zipFile.extract('bm_rates.dat')
    with open("bm_rates.dat", "r", encoding="windows-1251") as data_file:
        lst = []
        for line in data_file:
            lst.append(line.strip().split(';'))
        print(lst[0][0])
    os.remove("./bm_rates.dat")
        
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
