# Ingestão de dados no formado CSV no AWS S3 (Datalake para testes)
import boto3
import pandas as pd
import os
import sys
import threading

# 
# ATENÇÃO: O uso de credenciais fixos nos códigos NÃO é uma boa prática de segurança 
# e devemos evitar expor as credenciais, pois os serviços em nuvem são tarifados, no 
# código abaixo só está sendo utilizado por ser um caso especificamente para estudos, 
# então busque seguir a recomendação de segurança da AWS verificar a documentação em:
#
# https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/configuration.html
#
ACCESS_KEY='[AWS_ACCESS_KEY]'
SECRET_KEY='[AWS_SECRET_KEY]'

# Informe o caminho do download do arquivo 'microdados_educacao_basica_2020'
DIR_NAME=r'[PATH]'
# FILE_NAME=r'[FILE1; FILE2; ...]'
FILE_NAME= 'matricula_co.CSV;matricula_nordeste.CSV;matricula_norte.CSV;matricula_sudeste.CSV;matricula_sul.CSV'


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

#Criar cliente para interface de upload do arquivo com AWS S3
print('Definindo Client S3.')
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY   
)

## Lendo os arquivos
print('Lendo os arquivos.\n')
for fname in FILE_NAME.split(';'):

    arq = f'{DIR_NAME}\{fname}'
    print(f'Uploading [iniciando]: {arq}.')

    with open(arq, "rb") as f:

        s_dest = f'raw-data/censo/NU_ANO_CENSO=2020/{fname}'
        # excutando o upload para o S3
        s3_client.upload_fileobj(
            f, 
            "datalake-smedina-4343-igti-edc",                  
            s_dest,
            Callback=ProgressPercentage(arq)
        )

        f.close()
        print(f'\nUploading [finalizado]: {fname}\n\n')

print('\n\nFim.')


