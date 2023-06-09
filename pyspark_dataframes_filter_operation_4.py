# -*- coding: utf-8 -*-
"""Pyspark Dataframes- Filter operation 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LFWMeqaw9_ShNNdxYVPLwyhpg52AHiDO

### Pyspark Dataframes
- Filter Operation
- &,|,==
- ~
"""

!pip install pyspark

import pyspark

from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('dataframe').getOrCreate()

df_pyspark=spark.read.csv('test13.csv',header=True,inferSchema=True)
df_pyspark.show()

"""### Filter Operations"""

### Salary of the people less than or equal to 20000
df_pyspark.filter("Salary<=20000").show()

df_pyspark.filter("Salary<=20000").select(['Name','age']).show()

df_pyspark.filter(df_pyspark['Salary']<=20000).show()

df_pyspark.filter((df_pyspark['Salary']<=20000) | 
                  (df_pyspark['Salary']>=15000)).show()

df_pyspark.filter((df_pyspark['Salary']<=20000) &
                  (df_pyspark['Salary']>=15000)).show()

# ~ inverse /not
df_pyspark.filter(~(df_pyspark['Salary']<=20000)).show()











