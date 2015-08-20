import config
import requests
from HTMLtoPDFRederer import ToPDF
import argparse

class ArticleRequester:
    def __init__(self, url=config.settings['url'], alt_req_url='https://readability.com/api/content/v1/parser'):

        self.req_url = alt_req_url
        self.args = {
            'token' : config.settings['token'],
            'url' : url
        }


    def getArticle(self):
        #for some reason passing self.args doesnt work #FuckingMagic
        response = requests.get(self.req_url, {
            'token':self.args['token'],
            'url': self.args['url']
        })

        if response.status_code == requests.codes.ok:
            print("Response recieved. CODE: " + str(response.status_code))
            json_resp = response.json()
            content = json_resp['content']

        return content

    def savePDF(self, content):
      pdf = ToPDF(content)
      pdf.convert()

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
    args = parser.parse_args()
    req = ArticleRequester()
    content = req.savePDF(req.getArticle())
