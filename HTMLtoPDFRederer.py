import pdfkit



doc = ''
with open('content.html') as f:
   doc = f.read()

css = ''
with open('crayon.css') as f:
   css = f.read()

doc = '<html><head></head><body>' + doc + '</body></html>'

with open('newDOC.html', 'w') as f:
    f.write(doc)
pdfkit.from_string(doc,output_path='pdfka2.pdf', css='crayon.css')


