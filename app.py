from flask import Flask
from flask import render_template
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

@app.route('/')
def main():
    quota_url = ["https://api.api-ninjas.com/v2/randomquotes?categories=success,wisdom,life",
                 {"categories": "success,wisdom"},
                 {"X-Api-Key": "ZLZ1x2RdmfqoiZB5YuVJg4GNhLA1lmdI8lBfTEe9"}
            ]
    get_quota = requests.get(quota_url[0], params=quota_url[1], headers=quota_url[2])
    quota = get_quota.json()[0].get('quote')

    pic_url = "https://wallhaven.cc/api/v1/search?q=black&categories=100&purity=100&atleast=3840x1600&sorting=random&order=desc&colors=000000&seed=spgSur"
    get_pic_site = requests.get(pic_url)
    pic_site = get_pic_site.json().get('data')[random.randrange(0,8)].get('short_url')
    req_pic = requests.get(pic_site)

    soup = BeautifulSoup(req_pic.text, "html.parser")
    picture = soup.find('div', 'scrollbox').find('img').get('src')
    

    return render_template('index.html', quota = quota, picture = picture)

if __name__ == '__main__':
    app.run(debug=True)