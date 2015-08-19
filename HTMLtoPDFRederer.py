import pdfkit


class ToPDF:
    def __init__(self, doc, css = 'css/crayon.css'):
        self.doc = doc
        self.css = css

    def convert(self, output='out.pdf'):
        self.doc = '<html><head></head><body>' + self.doc + '</body></html>'
        pdfkit.from_string(self.doc, output_path=output, css=self.css)
