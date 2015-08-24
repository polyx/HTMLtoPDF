
# HTMLtoPDF
Converts articles on the web to the pdf.
Uses python 3.4 but should work on any 3.x

###Usage
`python main.py -u <article url>` or just `python main.py` and give set article url in config.py

###Dependencies
* pdfkit `pip install pdfkit` Note: might not work from virtualenv
* wkhtmltopdf which is required by pdfkit. To install go to http://wkhtmltopdf.org/
* requests `pip install requests`

