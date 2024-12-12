import urllib.request as request
import json

src="https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001277-053"
with request.urlopen(src) as response:
    # data = response.read()
    # data = response.read().decode(encoding='utf-8')

    data = json.load(response)
    for cell in data["result"]["records"]:
        print(cell)