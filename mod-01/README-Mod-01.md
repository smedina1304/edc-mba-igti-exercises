# edc-mba-igti-exercises
Exercícios dos Módulos do MBA IGTI - Engenheiro de Dados Cloud

## Módulo 01

### Trabalho prático:
<br>

1- Realizar o download dos MICRODADOS do ENEM 2019. 
<br>
O arquivo está disponível a partir deste link: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados>
<br>
Link direto para download: https://download.inep.gov.br/microdados/microdados_enem_2019.zip 
<br>

<p align="left">
   <img src="images\mod01-enem-001.png" width="400" style="max-width: 400px;">
</p>
<br>

Realizar o download em uma pasta local, descompactar e localizar na pasta `DATA` o arquivo `MICRODADOS_ENEM_2019.csv`.
<br>

Para realizar o download via código, utilizar como referência o programa abaixo:
<br>

Source: `mod-01\sources\mod01-trab-item1-download.py`
<br>

<br>

2- Criar um bucket chamado datalake-seunome-numerodaconta para armazenamento dos dados crus do ENEM 2019.
<br>
<p align="left">
   <img src="images\mod01-s3-001.png" width="400" style="max-width: 400px;">
</p>

<br>

3- Fazer a ingestão dos dados do ENEM 2019 em seu datalake em uma pasta intitulada `raw-data` utilizando o SDK de sua preferência ou a AWS CLI (`*Boto3 ou AWS CLI*` ).
<br>

Documentação de apoio:
<br>
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

- https://awscli.amazonaws.com/v2/documentation/api/latest/index.html 
<br>
<br>

Source: `mod-01\sources\mod01-trab-item3-ingestao-s3.py`
<br>
<br>
<p align="left">
   <img src="images\mod01-s3-003.png" width="400" style="max-width: 400px;">
</p>

<br>

4- Fazer a transformação do CSV em parquet utilizando spark
<br>

Para esta tarefa escolhi criar um JOB para rodar via AWS Glue, com Spark 24 e Python 3.
<br>

Source: `mod-01\sources\mod01-trab-item4-aws-glue-job_spark.py`
<br>
<br>
<p align="left">
   <img src="images\mod01-glue-001.png" width="400" style="max-width: 400px;">
</p>

<br>
<p align="left">
   <img src="images\mod01-glue-002.png" width="400" style="max-width: 400px;">
</p>
<br>



5- Escrever o parquet em uma outra pasta no bucket chamada `consumer-zone`.
<br>

Com o JOB acima (item 4) executado com sucesso, o arquivo parquet foi criado na pasta destino.
<br>
<br>
<p align="left">
   <img src="images\mod01-s3-004.png" width="400" style="max-width: 400px;">
</p>

<br>
<p align="left">
   <img src="images\mod01-s3-005.png" width="400" style="max-width: 400px;">
</p>
<br>

6- Criar e executar um Glue Crawler para disponibilizar o schema dos dados do ENEM 2019.
<br>

Iniciando a criação do Crawler.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-001.png" width="400" style="max-width: 400px;">
</p>
<br>

Selecionando o tipo da fonte dos dados.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-002.png" width="400" style="max-width: 400px;">
</p>
<br>

Definido o S3, o bucket e a pasta de dados criada no DataLake.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-003.png" width="400" style="max-width: 400px;">
</p>
<br>

Não será adicionado nenhuma outra fonte de dados.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-004.png" width="400" style="max-width: 400px;">
</p>
<br>

Definindo a role para utilização, no caso será criada uma nova automaticamente.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-005.png" width="400" style="max-width: 400px;">
</p>
<br>

Mantendo a frequencia default `por demanda` para atualização do catalogo de dados.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-006.png" width="400" style="max-width: 400px;">
</p>
<br>

Definindo o nome da `database` para disponibilização da tabela criada pelo crawler.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-007.png" width="400" style="max-width: 400px;">
</p>
<br>

Confirmando os dados e finalizando o processo.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-008.png" width="200" style="max-width: 200px;">
</p>
<br>

Selecionar o crawler e executar a função `Run`.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-009.png" width="400" style="max-width: 400px;">
</p>
<br>

Após alguns segundos é exibido a confirmação que o crawler disponibilizou a tabela na base de dados definida para acesso pelo AWS Athena.
<br>
<p align="left">
   <img src="images\mod01-glue-crawler-010.png" width="400" style="max-width: 400px;">
</p>
<br>


7- Realizar consultas SQL no AWS Athena.
<br>

Ao acessar o Athena, podemos verificar que a Database `datalake` foi disponibilizada e contém uma tabela disponível para consulta, sendo que o nome representa no mesmo da pasta do DataLake. Outro ponto muito importante é observar a mensagem que solicita a definição de um local de store para `query result`, a indicação é definir uma pasta especifica para esta função em seu datalake, caso não tenha recomenda-se criar uma pasta nova.
<br>
<p align="left">
   <img src="images\mod01-athena-001.png" width="400" style="max-width: 400px;">
</p>
<br>

Verificando o acesso aos dados da tabela virtualizada pelo crawler.
<br>
<p align="left">
   <img src="images\mod01-athena-002.png" width="400" style="max-width: 400px;">
</p>
<br>

Exemplo Query - 01.
<br>
<p align="left">
   <img src="images\mod01-athena-query-001.png" width="400" style="max-width: 400px;">
</p>
<br>

Exemplo Query - 02.
<br>
<p align="left">
   <img src="images\mod01-athena-query-002.png" width="400" style="max-width: 400px;">
</p>
<br>