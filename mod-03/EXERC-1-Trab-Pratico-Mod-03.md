# edc-mba-igti-exercises
Exercícios dos Módulos do MBA IGTI - Engenheiro de Dados Cloud

## Módulo 03


### Trabalho prático:

<br>

####1. Instalação Spark

- Para utilização do `pyspark`, é necessário a instalação do Python 3. ( https://www.python.org/ )<br>
    Para passo a passo: <br> https://phoenixnap.com/kb/how-to-install-python-3-windows

    <br>
    Seguem alguns links úteis:

    * [Tutorial de instalação do Spark no Windows](https://naomi-fridman.medium.com/install-pyspark-to-run-on-jupyter-notebook-on-windows-4ec2009de21f)
    * [Documentação do Spark](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html)

    <br>

- Instalação do Java, recomentado a versão 1.8.
  
    ```shell
        > java -version
    ```
    
    <p align="left">
    <img src="images\java-version-cmd.png" width="400" style="max-width: 400px;">
    </p>

    <br>

    Caso não tenha o Java instalado, fazer o download em https://java.com/en/download/, e realizar a instalação para o sistema operacional correspondente.

    <br>

    Passo a passo, junto com o próximo item.
    <br>


-  Download do Arquivo Spark.
    Link: https://spark.apache.org/downloads.html
    Verifique a versão indicada para sua utilização.

    <br>
    <p align="left">
    <img src="images\apache-spark-version.png" width="400" style="max-width: 400px;">
    </p>

    <br>

    Para passo a passo: <br> https://phoenixnap.com/kb/install-spark-on-windows-10


    <br>

-  Configuração de Variáveis de Ambiente.

    Devem ser definidas as seguintes variáveis de ambiente:
    - `JAVA_HOME` - para identificar a pasta de instalação do Java 1.8
    - `SPARK_HOME` - para informar a pasta de instalação do Apache Apark.
    - `HADOOP_HOME` - para informar a pasta de instalação do Hadoop, caso não existe nenhum recurso do Hadoop instalado na máquina, esta variável deve ter o mesmo conteúdo na `SPARK_HOME`.
    - `PATH` - a pasta com os binários do Java e Spark devem ser incluidos no path.

    <br>

    ##### Resultado pós Instalação.  


    Após instalação e finalização dos quatro pontos acima, o resultado ao executar o spark localmente deve ser similar a tela abaixo.
    <br>

    Console `scala` do Apache Spark.

    ```shell
        > spark-shell
    ```

    <p align="left">
    <img src="images\apache-spark-scala.png" width="500" style="max-width: 500px;">
    </p>

    Para sair.

    ```shell
        > sys.exit
    ```

    <br>

    Console `python` do Apache Spark.

    ```shell
        > pyspark
    ```

    <p align="left">
    <img src="images\apache-spark-pyspark.png" width="500" style="max-width: 500px;">
    </p>

    Para sair.

    ```shell
        >>> exit()
    ```

<br>
<br>

####2. Download dos Arquivos

- Será necessário fazer o download das tabelas no seguinte link: <br> https://datasets.imdbws.com/ 

    - `title.basics.tsv.gz`
    - `title.ratings.tsv.gz`

    <br>

    **Atenção:** <br>Será necessário descompactar os arquivos.<br>
    *Os arquivos neste projeto GIT, foram descompactados na pasta `/edc-mba-igti-exercises/mod-03/data/tsv`. Mas esta pasta **data** e suas sub-pastas não estarão disponíveis no projeto para minimizar espaço/tempo para download/upload com o Github, sendo exluidas pelo aqruivo `.gitignore`.* <br>
    Para montar a pasta conforme sugerido segue print abaixo.<br>

    <p align="left">
    <img src="images\pasta-data-files.png" width="200" style="max-width: 200px;">
    </p>

    <br>

    **Importante** <br>É necessário que os dados estejam localizados na mesma pasta em que o shell do Spark esteja sendo executado para que eles possam ser lidos de forma mais fácil. Por isso, observe bem onde a shell está sendo executada, ou mude o diretório da execução para a mesma pasta dos dados.

<br>
####3. Leitura dos Dados

- Para utilização dos dados no Spark, deve ser realizada a leitura dos dados. Execute os seguintes comandos em sequência: <br>

    ```shell
        >>> df_titles = spark.read.csv('title_basics.tsv', header=True, sep='\t')
    ```

    ```shell
        >>> df_ratings= spark.read.csv('title_ratings.tsv', header=True, sep='\t')
    ```

<br>
####4. Pacotes para interação com spark via Jupyter Notebook

<br>

- Instalar os pacotes:
    - pyspark
    - findspark (utilização Jupyter Notebook)

```shell
    >pip install pyspark findspark
```
<br>

####5. Analisar e exercitar com os códigos de exemplos como referência.

<br>

- Notebook(s)
    - `mod-03/sources/Exemplos_A1_Interativa.ipynb`

<br>
<br>

**ATENÇÃO:** 
A pasta `data` e suas `sub-pastas` não estarão disponíveis no projeto. (ver no item: *2 Download dos Arquivos*) <br>
Então ajustar nos códigos as referências dos paths de cada arquivo.

