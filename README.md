# hadoop-twitter-mapreduce
Streaming map reduce on Hadoop using python code

to run this example install hadoop following the given instuctions

```bash
# install java
sudo apt update -y
sudo apt install -y openjdk-8-jdk

# download hadoop
wget https://apachemirror.wuchna.com/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz

#extract hadoop
tar -xzf hadoop-3.3.0.tar.gz

# add paths to profile
cat <<EOT >> ~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/home/ubuntu/hadoop-3.3.0
export PATH=$PATH:/$HADOOP_HOME/sbin:/$HADOOP_HOME/bin
EOT
```
follow instructions further hadoop setup on https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html

```bash
# start all services if not already started
start-all.sh

# copy input filesd
hdfs dfs -p input
hdfs dfs -put ./sample-data input/sample-data

#run command
hadoop jar ./hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-input input/sample-data \
-mapper ./tweetMapper.py \
-reducer ./tweetReducer.py \
-output output -file *.py


hdfs dfs -cat output/* 
# or for truncated output first n lines
hdfs dfs -cat output/* | head -10
```

# LICENSE - MIT
