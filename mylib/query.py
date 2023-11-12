# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

def query():
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = (
        "SELECT Sex, AVG(Survived) as Survival "
        "FROM titanic_delta "
        "GROUP BY Sex "
    )
    query_result = spark.sql(query)
    return query_result

def viz():
    ## group by gender, calculate survival rate
    query_ = query().toPandas()
    print(query_)
    plt.bar(query_.Sex, query_.Survival)
    plt.title("Survival Rate for Titanic Passengers by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Rate")
    plt.show()



    ## group by PClass, calculate survival rate
    pass

if __name__ == "__main__":
    # print(type(query()))
    viz()