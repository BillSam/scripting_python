import PyPDF2

with open('./pdf/11.3 dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getPage(1))
