## Quick Start

To deploy an example HDFS cluster, run:

```
  docker-compose up
```

Connect to hdfs :

```
  docker exec -it namenode bash
  cd ~
```

```
apt-get update
apt-get install python3
apt-get install python3-pip
apt-get install cron
pip3 install requests
apt-get install nano && apt-get install default-jre
```

# Modifier le fichier /etc/hadoop/hadoop-env.sh

```
nano /etc/hadoop/hadoop-env.sh
```

# Décommenter la ligne JAVA_HOME et remplacer par

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

Add the following line to the end of the file and run service cron start:

```
crontab -e
```

```
service cron start
```

\* /12 \* \* \* python3 /root/code/app.py \* /6 \* \* \* cd /root/code/ && ./hadoop-launch.sh

Create a directory in HDFS:

```
  hdfs dfs -mkdir /data
```
