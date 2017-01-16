from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests
import urllib,urllib2
import random
import os
from string import strip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("MainPage.html")


@app.route('/getdata', methods = ['POST', 'GET'])
def getdata():
    if request.method == 'POST':
        url = request.form["url"]

        data_file = urllib2.urlopen(url)
        data_html = data_file.read()
        data_file.close()

        soup = BeautifulSoup(data_html, "html.parser")

        i = soup.find_all('img')

        for p in i:
            loc = p.get('src')
            r = random.randrange(1,1000)

            image_final = str(r) + ".jpg"

            if loc[:1] == '.':
                loc = loc.strip(loc[:1])
                image = str(url) + str(loc)

                urllib.urlretrieve(image, image_final)

            elif loc[:1] == '/':
                image = str(url) + str(loc)
                urllib.urlretrieve(image, image_final)

            else:
                urllib.urlretrieve(loc, image_final)

        return "<h1>Images have been Downloaded</h1>"


if __name__ == "__main__":
    app.run(debug = True)

