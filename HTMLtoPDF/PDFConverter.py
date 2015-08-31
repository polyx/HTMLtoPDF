import pdfkit
import os


class ToPDF:
    def __init__(self, doc, css = os.path.dirname(os.path.abspath(__file__)) + '\\..\\css\\bootstrap.css'):
        self.doc = doc
        self.css = css

    def convert(self, title = '', output='out.pdf'):
        self.doc = '<html><head></head><body><h1>' + title + '</h1><sbr>' + self.doc + '</body></html>'

        pdfkit.from_string(self.doc, output_path=output, css=self.css)
