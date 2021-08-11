# Ingestão de dados no formado CSV no AWS S3 (Datalake para testes)
import boto3
import pandas as pd
import os
import sys
import threading

# Entre com as credenciais nos parametros abaixo ou utilize o AWSCLI para 
# evitar expor no código as credenciais. Lembrando que esta não é uma prática 
# para aplicar em empresas, o caso abaixo só está sendo utiliza por ser um 
# caso de para estudos
ACCESS_KEY='[ACCESS_KEY]'
SECRET_KEY='[SECRET_KEY]'

# Informe o caminho do download do arquivo 'MICRODADOS_ENEM_2019.csv'
FILE_NAME=r'[PATH\FILENAME]'

# Classe para acompanhamento do percentual de upload
class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()



### Iniciando o processo de upload

# Criar cliente para interface de upload do arquivo com AWS S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY   
)

# Lendo o arquivo
with open(FILE_NAME, "rb") as f:

    # excutando o upload para o S3
    s3_client.upload_fileobj(
        f, 
        "datalake-smedina-4323-igti-edc",                  
        "raw-data/enem/year=2019/MICRODADOS_ENEM_2019.csv",
        Callback=ProgressPercentage(FILE_NAME)
    )


