import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from models.Sentence import Sentence, Base
from controllers.pdf_text_extractor import extract_text_from_file
from controllers.text_summarizer import summarize_text, get_title
from controllers.telegram_publisher import send_telegram_message
from controllers.load_data import load_data
from controllers.file_downloader import download_files, setup_download_path, get_file_paths
# import logging

# logging.basicConfig(level=logging.DEBUG)

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
DOWNLOAD_DIR = "https://sjconsulta.csjn.gov.ar/sjconsulta/novedades/consulta.html"
PDFS_BASE_URL = "https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoById.html?idDocumento="

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
buttonIds = load_data(DOWNLOAD_DIR)
pdfUrls = [PDFS_BASE_URL + doc_id for doc_id, title in buttonIds]
db = SQLAlchemy()
home_directory = os.path.expanduser('~')
sentencias_folder = os.path.join(home_directory, 'Desktop', 'Sentencias')
setup_download_path(sentencias_folder)
url_and_filenames = []
filenames = []
downloaded_sentencias = os.listdir(sentencias_folder)
print('Las sentencias se guardan en:', sentencias_folder)
sentencias_to_download = []
sentencias = []

def init_db():
  Base.metadata.create_all(bind=engine)

def add_sentence_to_db(sentence):
  session = SessionLocal()
  try:
    session.add(sentence)
    session.commit()
  except Exception as e:
    session.rollback()
  finally:
    session.close()

init_db()

for index, url in enumerate(pdfUrls):
  url_and_filenames.append((url, f'sentencia_{buttonIds[index][0]}.pdf', buttonIds[index][0]))
  filenames.append(f'sentencia_{buttonIds[index][0]}.pdf')
  sentencias.append(Sentence(url=url, id=buttonIds[index][0], sentence_title='', pdf_url='', full_text='', summary_text=''))

for sentencia in filenames:
  if sentencia not in downloaded_sentencias:
    print('Nueva sentencia para descargar: ', sentencia)
    sentencias_to_download.append(sentencia)

if len(sentencias_to_download) == 0:
  print('No hay nuevas sentencias para descargar. Nos vemos mañana!')
else:
  print('Vamos a descargar las siguientes sentencias: ', sentencias_to_download)
  button_ids_in_filenames = [filename.split('_')[1].split('.')[0] for filename in sentencias_to_download]
  print('Button IDs:', button_ids_in_filenames)
  filtered_url_and_filenames = [item for item in url_and_filenames if item[2] in button_ids_in_filenames]
  print("Filtered url and filenames", filtered_url_and_filenames)
  file_paths = []

  if len(filtered_url_and_filenames) > 0:
    print('Descargando nuevas sentencias...')
    file_paths = download_files(filtered_url_and_filenames, sentencias_folder)
  else:
    print('Obteniendo rutas de archivos ...')
    file_paths = get_file_paths(sentencias_folder)

  print('Vamos a resumir y publicar las siguientes sentencias: ', file_paths)

  session = SessionLocal()
  try:
    for path in file_paths:
      id = path.split('sentencia_')[1].split('.')[0]
      print('Extrayendo texto de la sentencia ', id)
      text = extract_text_from_file(path)
      summary = summarize_text(text)
      print('El resumen de la sentencia es: ', summary)
      send_telegram_message(summary)
      sentence = session.query(Sentence).filter_by(id=id).first()
      
      if sentence:
        sentence.pdf_url = path
        sentence.title = get_title(summary)
        sentence.full_text = text
        sentence.summary_text = summary
        print('Nueva sentencia para guardar en la base de datos: ', sentence)
        add_sentence_to_db(sentence)
  finally:
    session.close()
