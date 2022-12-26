# using PySpark to split data and create multiple files containing specific user data

#create spark session and import parent data
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("appName").getOrCreate()
df = spark.read.csv('file.csv',inferSchema=True,header=True)

#want to edit/adjust dataframe here
#todo - change sender column from json to string (want Address property specifically)
schema = 
df.withColumn("sender",from_json(df.Sender),schema)

#get a count of each item for the file (info)
countdata = df.groupby('LName').count().show()

#get a list of unique values for LName
lname_values = df.select('LName').distinct().collect()

#loop and create a new DF for each unique user, convert to HTML(using pandas) and save to a new file.
for user in lname_values:
	user_data = df.filter((df.LName).isin([user[0]])).collect()
	userDF = spark.createDataFrame(user_data)
	out_data = userDF.topandas().to_HTML()

	mssparkutils.fs.put("c:\temp" + "out_file", out_data, True) #this is an azure spark utility
