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

        image_list = []

        for p in i:
            loc = p.get('src') # Get the source url of the image
            l = len(loc) # Get the length of the url

            # print loc[l-3] # Get the third last character for the type of image

            r = random.randrange(1,1000)

            if loc[l-3] == 'p': # For png Image
                if loc[:1] == ".":
                    loc = loc.strip(loc[:1])
                    final_url = str(url) + str(loc)
                    image_list.append(final_url)
                    final_image = str(r) + ".png"
                    urllib.urlretrieve(final_url, final_image)

                elif loc[:1] =='/':
                    final_url = str(url) + str(loc)
                    image_list.append(final_url)
                    final_image = str(r) + ".png"
                    urllib.urlretrieve(final_url, final_image)

                else:
                    image_list.append(loc)
                    r = random.randrange(1,1000)
                    final_image = str(r) + ".png"
                    urllib.urlretrieve(loc, final_image)

            elif loc[l-3] == 'j': # For jpg Image
                if loc[:1] == ".":
                    loc = loc.strip(loc[:1])
                    final_url = str(url) + str(loc)
                    image_list.append(final_url)
                    final_image = str(r) + ".jpg"
                    urllib.urlretrieve(final_url, final_image)

                elif loc[:1] == '/':
                    final_url = str(url) + str(loc)
                    image_list.append(final_url)
                    final_image = str(r) + ".jpg"
                    urllib.urlretrieve(final_url, final_image)

                else:
                    image_list.append(loc)
                    r = random.randrange(1, 1000)
                    final_image = str(r) + ".jpg"
                    urllib.urlretrieve(loc, final_image)

        print "Total Images in the webpage : "  + str(len(image_list))
        print image_list

        return "<h1 align='center'>The Images have been Downloaded</h1>"


if __name__ == "__main__":
    app.run(debug = True)

