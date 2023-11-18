import requests
from bs4 import BeautifulSoup

def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = [link['href'] for link in soup.find_all('a', class_='pdf-link')]
    return pdf_links