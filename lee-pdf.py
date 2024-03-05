import os
import PyPDF2

os.chdir('D:\\Isapre')
lista = os.listdir()
pdf_files = [f for f in lista if f.endswith(".pdf")]
print(pdf_files)

# Open the PDF file
pdf_file = open('CartaDesafiliacion agos 2020.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Iterate over the pages in the PDF file
for page_num in range(num_pages):

    # Get the page object
    page = pdf_reader.pages[page_num]

    # Extract the text from the page

    text = page.extract_text()


    # Print the text from the page
    print(text)

# Close the PDF file
pdf_file.close()
