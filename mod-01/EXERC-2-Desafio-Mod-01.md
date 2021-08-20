# edc-mba-igti-exercises
Exercícios dos Módulos do MBA IGTI - Engenheiro de Dados Cloud

## Módulo 01

### Desafio-Mod-01:
<br>

`ATENÇÃO:`
*Toda a infraestrutura em nuvem deve ser implantada utilizando o Terraform (ou outra solução de IaC de sua escolha) e esteiras de deploy no Github (ou Gitlab, ou Bitbucket, ou outro de sua escolha).*
<br>
<br>

`Preparação da Infraestrutura em Nuvem:`
*Utilizando IaC com esteira de Deploy no Github.*
<br>

Toda infraestrutura para esta etapa foi criada utilizando o Terraform, e os scripts estão na pasta: `mod-01/infraestrutura` com os arquivos separados por recurso ou funcionalidade.
<br>

Foram executados os procedimento com o Terraform para validar os scripts:
<br>

```console
terraform init

terraform fmt

terraform validate

terraform plan
```
<br>
<br>

1- Realizar a ingestão dos dados do Censo Escolar 2020 no AWS S3 ou outro storage de nuvem de sua escolha. Dados disponíveis em: `https://www.gov.br/inep/ptbr/acesso-a-informacao/dados-abertos/microdados/censo-escolar`. O método de ingestão é livre. Os dados devem ser ingeridos na zona raw ou zona crua ou zona 
bronze do seu Data Lake. 

<br>

2- Utilizar alguma tecnologia de Big Data para transformar os dados no formato parquet
e escrevê-los na zona staging ou zona silver do seu Data Lake.

<br>

3- Fazer a integração com alguma engine de Data Lake. No caso da AWS, você deve:
a. Configurar um Crawler para a pasta onde os arquivos na staging estão 
depositados;
b. Validar a disponibilização no Athena.

<br>

4- Caso deseje utilizar o Google, disponibilize os dados para consulta usando o Big 
Query. Caso utilize outra nuvem, a escolha da engine de Data Lake é livre.

<br>

5- Use a ferramenta de Big Data ou a engine de Data Lake (ou o BigQuery, se escolher 
trabalhar com Google Cloud) para investigar os dados e responder às perguntas do 
desafio.

<br>

6- Quando o desenho da arquitetura estiver pronto, crie um repositório no Github (ou 
Gitlab, ou Bitbucket, ou outro de sua escolha) e coloque o código IaC para a 
implantação da infraestrutura. Nenhum recurso deve ser implantado 
manualmente

