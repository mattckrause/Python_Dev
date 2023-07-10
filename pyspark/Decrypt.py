#Create a pyspark function to decrypt data gathered from Microsoft Graph Data Connect cross tenant data extraction.
#This function will be used in the pyspark script to decrypt the data.	


#Import the required libraries
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

#Define the function to decrypt the data
def decrypt_data(data, key):
    #Decode the data from base64
	data = base64.b64decode(data)
	#Get the initialization vector from the data
	iv = data[:AES.block_size]
	#Create the cipher object
	cipher = AES.new(key, AES.MODE_CBC, iv)
	#Decrypt the data
	decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
	#Return the decrypted data
	return decrypted_data.decode('utf-8')

#Define the function to get the key from the secret
def get_key(secret):
	#Create a hash object
	hash_object = hashlib.sha256(secret.encode('utf-8'))
	#Get the hash digest
	hex_dig = hash_object.hexdigest()
	#Return the key
	return hex_dig[:32]

#unpack gzip file
def unpack_gzip(data):
	#Import the required libraries
	import gzip
	import io
	#Create a gzip object
	gzipper = gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb')
	#Return the decompressed data
	return gzipper.read()

#pyspark code to read a file from Azure Data Lake Storage Gen2 decompress the gzip file and decode utf-8
#Import the required libraries
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
import gzip
import io

#Define the function to decrypt the data
def decrypt_data(data, key):
	#Decode the data from base64
	data = base64.b64decode(data)
	#Get the initialization vector from the data
	iv = data[:AES.block_size]
	#Create the cipher object
	cipher = AES.new(key, AES.MODE_CBC, iv)
	#Decrypt the data
	decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
	#Return the decrypted data
	return decrypted_data.decode('utf-8')

#Define the function to get the key from the secret
def get_key(secret):
	#Create a hash object
	hash_object = hashlib.sha256(secret.encode('utf-8'))
	#Get the hash digest
	hex_dig = hash_object.hexdigest()
	#Return the key
	return hex_dig[:32]

#Define the function to unpack gzip file
def unpack_gzip(data):
	#Create a gzip object
	gzipper = gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb')
	#Return the decompressed data
	return gzipper.read()

#Create a UDF to decrypt the data
decrypt_data_udf = udf(decrypt_data, StringType())

#Create a UDF to unpack gzip file
unpack_gzip_udf = udf(unpack_gzip, StringType())

#Read the file from Azure Data Lake Storage Gen2
df = spark.read.format("com.springml.spark.sftp").option("host", "sftpserver").option("username", "sftpuser").option("password", "sftppassword").option("fileType", "csv").option("delimiter", "|").load("/data/encrypted_data.csv")

#Get the key from the secret
