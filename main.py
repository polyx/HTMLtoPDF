import config
import requests
import HTMLtoPDFRederer


req_url = 'https://readability.com/api/content/v1/parser'
args = {
    'url' : config.settings.url,
    'token' : config.settings.token
}
response = requests.get(req_url, args)
if response.status_code == requests.codes.ok:
    print("Response recieved.")
    json_resp = response.json()
    content = json_resp['content']
#DEBUG help
# with open('content.html','w') as f:
#     f.write(content)
# with open("response.json", 'w') as response_json:
#     response_json.write(response.text)
#     response_json.close()


