import argparse
import os

import requests
from . import config
from .PDFConverter import ToPDF

__version__ = '0.0.1'

class ArticleRequester:
    def __init__(self, url=config.settings['url'],
                 token=config.settings['token'],):
        self.urls = url
        self.response = None
        self.req_url = 'https://readability.com/api/content/v1/parser'
        self.token = token

    def getArticle(self):
        # for some reason passing self.args to .get() doesnt work #FuckingMagic
        articles = []

        for url in self.urls:
            print(url)
            response = requests.get(self.req_url, {
                'token': self.token,
                'url'  : url
            })
            if response.status_code == requests.codes.ok:
                print("Response recieved. CODE: " + str(response.status_code))
                json_resp = response.json()
                self.response = json_resp
                articles.append({
                    'body':json_resp['content'],
                    'title':json_resp['title']
                })

        return articles

    def savePDF(self, content):
        pdf = ToPDF(content)
        pdf.convert()

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
    articles = req.getArticle()
    response = req.response
    req.savePDF(articles)
