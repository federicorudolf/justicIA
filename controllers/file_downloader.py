import os
import requests

def setup_download_path(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
  return directory

def download_files(urls_and_filenames, directory):
  file_paths = []
  for index, tuple in enumerate(urls_and_filenames):
    url, filename, id = tuple
    if not os.path.exists(directory):
      os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    print('Descargando sentencia: ', file_path)
    if not file_path.lower().endswith('.pdf'):
      file_path += '.pdf'

    response = requests.get(url, stream=True, verify=False)
    if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
      with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
          if chunk:
            file.write(chunk)
      print(f"PDF guardado en {file_path}")
      file_paths.append(file_path)
    else:
      print(f"Hubo un problema guardando el PDF. Codigo del error: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")
  return file_paths
  
def get_file_paths(directory):
  file_paths = []
  for filename in os.listdir(directory):
    full_path = os.path.join(directory, filename)
    if os.path.isfile(full_path):
      file_paths.append(full_path)
  return file_paths
