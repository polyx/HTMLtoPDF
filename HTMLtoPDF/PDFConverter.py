import pdfkit
import os
import time


class ToPDF:
    def __init__(self, docs, css = os.path.dirname(os.path.abspath(__file__)) + '\\..\\css\\bootstrap.css'):
        '''

        :param docs: list of dicts containing title and body of the articles to be converted
        :param css:  alternative css file to be aplied to the pdf
        :return:
        '''

        self.docs = docs
        self.css = css

    def convert(self):
        prepared_docs = []
        file_names = []
        counter = 0
        for doc in self.docs:
            with open(str(counter) + '.html', 'w') as f:
                file_names.append(str(counter) + '.html')
                css = '<link rel="stylesheet" type="text/css" href="' + self.css + '">'
                f.write('<html><head>'+ css +'</head><body><h1>' + doc['title'] + '</h1><br>' + doc['body'] + '</body></html>')
                counter += 1

        for file in file_names:
            prepared_docs.append(file)
            print(file)

        start_time = time.time()
        pdfkit.from_file(prepared_docs, output_path='output.pdf')
        print("---converted in %s seconds ---" % (time.time() - start_time))
