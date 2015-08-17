import config
import requests
import HTMLtoPDFRederer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('URL', help='URL with article to be converted to pdf article')
parser.add_argument('-o', '--output', help='Output file name without extension(Always pdf)' )
args = parser.parse_args()

if args.output:
    print(args.output)
else:
    print(args.URL)


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
with open('etc/content.html','w') as f:
   f.write(content)
with open("etc/response.json", 'w') as response_json:
   response_json.write(response.text)
   response_json.close()


