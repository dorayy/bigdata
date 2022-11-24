#!/bin/bash

for entry in /root/data/*.json
do
        /opt/hadoop-3.2.1/bin/hdfs dfs -put "${entry}" /