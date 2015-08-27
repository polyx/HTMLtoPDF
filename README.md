
# HTMLtoPDF
Converts articles on the web to the pdf.
Uses python 3.4 but should work on any 3.x

###Usage
`python -m HTMLtoPDF -u <article url>` or just install with `python setup.py install`
than you can run it just with `HTMLtoPDF -u <article ur>`

Make sure to make `config.py` form `config_example.py` and put it into HTMLtoPDF folder

###Dependencies
* pdfkit `pip install pdfkit` Note: might not work from virtualenv
* wkhtmltopdf which is required by pdfkit. To install go to http://wkhtmltopdf.org/
* requests `pip install requests`


###Known issues
Does not handle code snipets well - no monospace font or other forms of special formating is applied to code snippets. If you have ideas how to detect code snippets and format them nicely feel free to send a pull request.