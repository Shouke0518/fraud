from flask import Flask, render_template
import urllib.request as request
import json

app = Flask(__name__)

# src="https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001277-053"
# with request.urlopen(src) as response:
#     data = json.load(response)

# @app.route('/')
# def index():
#     return render_template("fraud_list.html", data = data)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()