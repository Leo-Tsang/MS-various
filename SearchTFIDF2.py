from pyspark.sql import SQLContext
from pyspark.sql.functions import *

#reads the table that I have already saved
tfidf = sqlContext.read.format('csv').load('/user/root/tfidf', header='true')

#the UDF that I have created to search/index the table you have to enter the word separate by a comma, for it to work
def search(query1,query2,N):
    #create a subset of the query word
    temp1 = tfidf.filter(col('word') == query1).orderBy('tf_idf', ascending=False).select('article', 'word',
                                                                                             'tf_idf')
    #create subset of another query word
    temp2 = tfidf.filter(col('word') == query2).orderBy('tf_idf', ascending=False).select('article', 'word',
                                                                                                'tf_idf')

    #combines the two word searched earlier, and set up for recalcualtion of tf_idf
    tempjoin = temp1.union(temp2).orderBy('tf_idf', ascending=False).withColumn('weight', lit(1))

    #casting tf_idf to double so i can do computations
    tempjoin.withColumn('tf_idf', tempjoin['tf_idf'].cast('double'))

    #consolidate the table before and calculate the new tf_idf

    consolidate = tempjoin.groupby('article').agg(sum('tf_idf') * (sum('weight') / 2)).withColumnRenamed(
        '(sum(tf_idf) * (sum(count) / 2))', 'tf_idf').orderBy('tf_idf', ascending=False)

    return(consolidate.show(N))


