# MetaWeather API: Cities Average Maximum Temperature 

# import module
import math
import threading
from warnings import filterwarnings
filterwarnings('ignore')
import urllib.parse
import urllib.request
import ast
import threading


# Sparsing the City Salt Lake City, Los Angeles, Boise Data and svaing in text file
def url_retrieve():

    # Salt Lake City
    url1 = " https://www.metaweather.com/api/location/2487610/" 
    urllib.request.urlretrieve(url1,"salt_lake_city_data.txt" )

    # Los Angeles
    url2 = "https://www.metaweather.com/api/location/2442047/" 
    urllib.request.urlretrieve(url2,"los_angeles_data.txt")

    # Boise
    url3 = " https://www.metaweather.com/api/location/2366355/" 
    urllib.request.urlretrieve(url3,"boise_data.txt")

x = threading.Thread(target=url_retrieve)
x.start()

#Reading data text file and creating a dictionary type for each city

# Salt Lake City
file1 = open('salt_lake_city_data.txt', 'r')
contents1 = file1.read()
salt_lake_city_dictionary = ast.literal_eval(contents1)
print(salt_lake_city_dictionary)

# Los Angeles
file2 = open('los_angeles_data.txt', 'r')
contents2 = file2.read()
los_angeles_dictionary = ast.literal_eval(contents2)
#print(los_angeles_dictionary)
file2.close()

# Boise
file3 = open('boise_data.txt', 'r')
contents3 = file3.read()
boise_dictionary = ast.literal_eval(contents3)
#print(boise_dictionary)
file3.close()

# Define average of a list Function
def average_func(l):
    average = round( sum(l) / len(l),2)
    return average
	
	
# List of max_temperature
    
# Salt Lake City
max_temperature_s= []
for i in range(len(salt_lake_city_dictionary['consolidated_weather'])):
    max_temperature_s.append(salt_lake_city_dictionary['consolidated_weather'][i]['max_temp'])
#print(max_temperature_s)

# Los Angeles
max_temperature_l= []
for i in range(len(los_angeles_dictionary['consolidated_weather'])):
    max_temperature_l.append(los_angeles_dictionary['consolidated_weather'][i]['max_temp'])
#print(max_temperature_l)
    
# Boise
max_temperature_b= []
for i in range(len(boise_dictionary['consolidated_weather'])):
    max_temperature_b.append(boise_dictionary['consolidated_weather'][i]['max_temp'])
#print(max_temperature_b)

# Average Max temperature list

# Salt lake city average maximum temperature
salt_lake_city_aveg_max_temp = average_func(max_temperature_s)
  

 # Los Angeles average maximum temperature
los_angeles_aveg_max_temp = average_func(max_temperature_l)
   

# Boise average maximum temperature
boise_aveg_max_temp = average_func(max_temperature_b)

# Results
print("Salt Lake City Average Max Temp: ", salt_lake_city_aveg_max_temp)
print("Los Angeles Average Max Temp: ", los_angeles_aveg_max_temp)
print("Boise Average Max Temp: ", boise_aveg_max_temp)
