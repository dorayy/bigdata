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

Créer le repertoire data sur la machine namenode et récupérer les datas:

```
  mkdir data
  python app.py
```
