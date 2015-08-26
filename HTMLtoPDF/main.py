import argparse
import os

import requests
from . import config
from .PDFConverter import ToPDF

__version__ = '0.0.1'




class ArticleRequester:
    def __init__(self, url=config.settings['url'],
                 token=config.settings['token'],
                 alt_req_url='https://readability.com/api/content/v1/parser'):
        self.response = None
        self.req_url = alt_req_url
        self.args = dict(token=config.settings['token'], url=url)

    def getArticle(self):
        # for some reason passing self.args to .get() doesnt work #FuckingMagic
        response = requests.get(self.req_url, {
            'token': self.args['token'],
            'url': self.args['url']
        })

        if response.status_code == requests.codes.ok:
            print("Response recieved. CODE: " + str(response.status_code))
            json_resp = response.json()
            self.response = json_resp
            content = json_resp['content']

        return content

    def savePDF(self, content, title=''):
        pdf = ToPDF(content)
        pdf.convert(title=title)

    def writeDebugFiles(self):
        with open('etc/content.html', 'w') as f:
            f.write(self.content)
        with open("etc/response.json", 'w') as response_json:
            response_json.write(self.response.text)
            response_json.close()


def main():
    print('PATH: ' + os.path.dirname(os.path.abspath(__file__)))
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        help='URL with article to be converted to pdf article')
    args = parser.parse_args()
    if args.u:
        req = ArticleRequester(url=args.u)
    else:
        req = ArticleRequester()
    article = req.getArticle()
    response = req.response
    req.savePDF(article, title=response['title'])
