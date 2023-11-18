import PyPDF2
import requests
import pdfplumber

def extract_text_from_pdf(pdf_link):
    response = requests.get(pdf_link)
    with open('temp.pdf', 'wb') as pdf_file:
        pdf_file.write(response.content)
    
    with open('temp.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def extract_text_from_local_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                text += "[Text could not be extracted from this page]"
        return text
    
def extract_text_from_file(pdf_path):
    print('Extracting: ', pdf_path)
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or "[Text could not be extracted from this page]"
    return text

