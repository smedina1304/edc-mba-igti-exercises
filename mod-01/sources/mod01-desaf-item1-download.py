import requests
import zipfile
import os
from io import BytesIO


# Link para download do arquivo do enam
csvUrl = 'https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2020.zip'

# Path do diretorio para gravação do arquivo
#dirPath = '[INFORMAR PATH P/ DOWNLOAD]'
dirPath = './Downloads'

# Iniciando o download
filebytes = BytesIO(
    requests.get(csvUrl).content
)

# Extraindo o conteúdo do arquivo
fileZip = zipfile.ZipFile(filebytes)
fileZip.extractall(dirPath)
