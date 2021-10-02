####Link: 
https://medium.com/beeranddiapers/installing-apache-spark-on-mac-os-ce416007d79f


```shell
brew install apache-spark
```


####Editar profile

```shell
nano ~/.zprofile
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_271.jdk/Contents/Home
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.1.2/libexec
export HADOOP_HOME=/usr/local/Cellar/apache-spark/3.1.2/libexec
```
