# edc-mba-igti-exercises
Exercícios dos Módulos do MBA IGTI - Engenheiro de Dados Cloud

## Módulo 01

### Trabalho prático:
1. Realizar o download dos MICRODADOS do ENEM 2019. O arquivo está disponível neste link: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados>
<br>
Link direto para download: https://download.inep.gov.br/microdados/microdados_enem_2019.zip 
<br>

*(Baixar em uma pasta local, descompactar o arquivo e localizar em DATA o arquivo `MICRODADOS_ENEM_2019.csv`)*
<br>

<br>
<p align="left">
   <img src="images\mod01-enem-001.png" width="400" style="max-width: 400px;">
</p>
<br>

2. Criar um bucket chamado datalake-seunome-numerodaconta para armazenamento dos dados crus do ENEM 2019.
<br>
<p align="left">
   <img src="images\mod01-s3-001.png" width="400" style="max-width: 400px;">
</p>

<br>

3. Fazer a ingestão dos dados do ENEM 2019 em seu datalake em uma pasta intitulada `raw-data` utilizando o SDK de sua preferência ou a AWS CLI (`*Boto3 ou AWS CLI*` ).
<br>

Documentação de apoio:
<br>
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

- https://awscli.amazonaws.com/v2/documentation/api/latest/index.html 
<br>
<br>

Source: `*mod-01\sources\mod01-trab-item3-ingestao-s3.py*`
<br>
<br>
<p align="left">
   <img src="images\mod01-s3-003.png" width="400" style="max-width: 400px;">
</p>

<br>

4. Fazer a transformação do CSV em parquet utilizando spark

5. Escrever o parquet em uma outra pasta no bucket chamada consumer-zone.

6. Criar e executar um Glue Crawler para disponibilizar o schema dos dados do ENEM 2019.

7. Realizar consultas SQL no AWS Athena.

