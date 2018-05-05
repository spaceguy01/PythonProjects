""" Using PyPDF2 for Reading and Editing PDF Files """

import PyPDF2

""" Open the PDF in Binary Read mode """
pdfFile = open('sample.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdfFile)

""" Get number of pages in PDF File """
print (pdf.numPages)

""" Get a specific page in PDF and extract Text from PDF """
page = pdf.getPage(0)
page_text = page.extractText()
print (page_text)

""" Extracting Text from all PDF pages in the file """
for pageNum in range(pdf.numPages):
    print (pdf.getPage(pageNum).extractText())


""" COMBINING TWO PDF FILES """
pdf1 = open('sample.pdf', 'rb')
pdf2 = open('sample1.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)

writer = PyPDF2.PdfFileWriter()

""" Loop through both pdf to get pages """
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

"""Create output file to combine both pdf in Write Binary mode """
output = open('combinedPDF.pdf', 'wb')
writer.write(output)

""" close all open pdf files after creating the combinedPDF as output"""
output.close()
pdf1.close()
pdf2.close()
