from flask import Flask
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/')
def index():
    resp = urlopen('http://api.bestchange.ru/info.zip')
    zipfile = ZipFile(BytesIO(resp.read()))
    data = zipfile.read('bm_rates.dat')
    with open(data) as zipfile:
        for line in zipfile:
            line_list = line.strip('\n').split(';')
            print(f'{float (line_list [0])}   {float (line_list [1]):.5f}')

    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
