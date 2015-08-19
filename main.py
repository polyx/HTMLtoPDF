import config
import requests
import HTMLtoPDFRederer
import argparse

class ArticleRequester:
    def __init__(self, url=config.settings['url']):

        self.req_url = 'https://readability.com/api/content/v1/parser'
        self.args = {
            'token' : config.settings['token'],
            'url' : url
        }


    def getArticle(self):
        response = requests.get(self.req_url, args)

        if response.status_code == requests.codes.ok:
            print("Response recieved. CODE: " + response.status_code)
            json_resp = response.json()
            content = json_resp['content']

        return content


    def writeDebugFiles(self):
        with open('etc/content.html','w') as f:
            f.write(self.content)
        with open("etc/response.json", 'w') as response_json:
            response_json.write(self.response.text)
            response_json.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('URL', 
      help='URL with article to be converted to pdf article')
    parser.add_argument('-o', '--output', 
      help='Output file name without extension(Always pdf)' )
    args = parser.parse_args()
    if args.output:
        print(args.output)
    else:
        print(args.URL)
