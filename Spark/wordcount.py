import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <input-file> <output-file>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext("local","PySpark Word Count Exmaple")

    words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
    wordCounts.saveAsTextFile(sys.argv[2])
