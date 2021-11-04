from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    rs = requests.get('http://api.scraperapi.com/?api_key=60c8bd0701f81a48bf8a2fd08e79c35e&url=https://www.bestchange.ru/ripple-to-yoomoney.html')
    root = BeautifulSoup(rs.content, 'html.parser')

    for tr in root.select('#content_table > tbody > tr'):
        name = tr.select_one('td.bj .pc .ca').get_text(strip=True)
        [give_el, get_el] = tr.select('td.bi')
        give = give_el.select_one('.fs').get_text(strip=True)
        get = get_el.get_text(strip=True)
        print(name, give, get, sep=' | ')

    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
