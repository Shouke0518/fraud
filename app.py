from flask import Flask, render_template
import urllib.request as request
import json
from urllib.error import URLError

app = Flask(__name__)

try:
    with urllib.request.urlopen(src, timeout=10) as response:
        data = response.read()
        print("Data fetched successfully:", data)
except URLError as e:
    print("Failed to fetch URL:", e)
except TimeoutError:
    print("Request timed out")

@app.route('/')
def index():
    return render_template("fraud_list.html", data = data)

if __name__ == '__main__':
    app.run()