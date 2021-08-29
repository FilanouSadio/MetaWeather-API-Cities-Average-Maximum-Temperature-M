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

def create_dictionary(fichier):
    file = open(fichier, 'r')
    contents = file.read()
    city_dictionary = ast.literal_eval(contents)
    file.close()
    return city_dictionary

#Call the function  create_dictionary

# Salt Lake City
salt_lake_city_dictionary = create_dictionary('salt_lake_city_data.txt')

# Los Angeles
los_angeles_dictionary = create_dictionary('los_angeles_data.txt')

# Boise
boise_dictionary = create_dictionary('boise_data.txt')

# Define average of a list Function
def average_func(l):
    average = round( sum(l) / len(l),2)
    return average
	
# Function average_max for city average maximum temperature

def average_max(city_dict):
    max_temperature= []
    for i in range(len(city_dict['consolidated_weather'])):
        max_temperature.append(city_dict['consolidated_weather'][i]['max_temp'])
    city_aveg_max_temp = average_func(max_temperature)
    return  city_aveg_max_temp
    
# Call the function average_max

# Salt lake city average maximum temperature
salt_lake_city_aveg_max_temp =average_max(salt_lake_city_dictionary)
  
# Los Angeles average maximum temperature
los_angeles_aveg_max_temp = average_max(los_angeles_dictionary)
   

# Boise average maximum temperature
boise_aveg_max_temp = average_max(boise_dictionary)

# Results
print("Salt Lake City Average Max Temp: ", salt_lake_city_aveg_max_temp)
print("Los Angeles Average Max Temp: ", los_angeles_aveg_max_temp)
print("Boise Average Max Temp: ", boise_aveg_max_temp)
