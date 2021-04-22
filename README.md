# hadoop-twitter-mapreduce
Streaming map reduce on Hadoop using python code

to run this example


```bash
hadoop jar ./hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -input input/sample-data -mapper ./tweetMapper.py  -reducer ./tweetReducer.py -output output -file *.py
```


# LICENSE - MIT
