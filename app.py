from flask import Flask
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import os
import json

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
    getSell = "BTC"
    getBuy = "ETH"
    with open('valueArray.json') as f:
        value = json.load(f)
        idSell = int("".join([str(i["id"])
                              for i in value if i["key"] == getSell]))
        idBuy = int("".join([str(i["id"])
                            for i in value if i["key"] == getBuy]))
        strValue = []
        for i in lst:
            if int(i[0]) == idSell and int(i[1]) == idBuy:
                strValue.append(i)
        for i in strValue:
            if float(i[3]) > float(i[4]):
                sortedStrValueDown = sorted(
                    strValue, key=lambda x: (-float(x[4]), float(x[3])))
                print(sortedStrValueDown)
                break
            elif float(i[3]) < float(i[4]):
                sortedStrValueUp = sorted(
                    strValue, key=lambda x: (-float(x[3]), float(x[4])))
                print(sortedStrValueUp)
                break
    os.remove("./bm_rates.dat")

    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
