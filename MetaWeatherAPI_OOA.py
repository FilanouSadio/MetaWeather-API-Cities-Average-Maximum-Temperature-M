# MetaWeather API: Cities Average Maximum Temperature Object-Oriented Approach (OOA)

# Immport math library
import math
# import module
import urllib.request
import ast


# Parsing the City Salt Lake City, Los Angeles, Boise Data
class ExtractCityData:
    def __init__(self,url,output_file):
        self.url = url
        self.output_file = output_file

    # Instance  url_retrieve 
    def url_retrieve(self):
        urllib.request.urlretrieve(self.url, self.output_file )

# Data Transformation to dictionary Type
class TransformToDictionary:
    def __init__(self,fichier):
        self.fichier = fichier

    # Instance  create_dictionary 
    def create_dictionary(self):
        file = open(self.fichier, 'r')
        contents = file.read()
        city_dictionary = ast.literal_eval(contents)
        file.close()
        return city_dictionary

# Average Maximum Temperature
class AverageMaxTemp():
    def __init__(self,city_dict):
        self.city_dict = city_dict

    #Average of a list Function 

    @staticmethod 
    # Static Method average_func
    def average_func(l):
        average = round( sum(l) / len(l),2)
        return average

    # Instance  average_max   
    def average_max(self):
        max_temperature= []
        for i in range(len(self.city_dict['consolidated_weather'])):
            max_temperature.append(self.city_dict['consolidated_weather'][i]['max_temp'])
        city_aveg_max_temp = self.average_func(max_temperature)
        return  city_aveg_max_temp
		
# Main Execution
if __name__ == "__main__":

    # Data Extraction

    # Salt Lake City data
    ExtractCityData("https://www.metaweather.com/api/location/2487610/", "salt_lake_city_dataOOA.txt").url_retrieve()

    # Los Angeles data
    ExtractCityData("https://www.metaweather.com/api/location/2442047/", 'los_angeles_dataOOA.txt').url_retrieve() 

    # Boise data
    ExtractCityData("https://www.metaweather.com/api/location/2366355/", 'boise_dataOOA.txt').url_retrieve() 
    
    # Data Transformation

    # Salt Lake City

    salt_lake_city_dictionary = TransformToDictionary('salt_lake_city_dataOOA.txt').create_dictionary()

    # Los Angeles
    los_angeles_dictionary = TransformToDictionary('los_angeles_dataOOA.txt').create_dictionary()

    # Boise
    boise_dictionary = TransformToDictionary('boise_dataOOA.txt').create_dictionary()   
    
    # Average Maximum Temperature
    
    salt_lake_city_aveg_max_temp = AverageMaxTemp(salt_lake_city_dictionary).average_max()
    los_angeles_aveg_max_temp = AverageMaxTemp(los_angeles_dictionary).average_max()
    boise_aveg_max_temp = AverageMaxTemp(boise_dictionary).average_max()

# Results
    print("Salt Lake City Average Max Temp: ", salt_lake_city_aveg_max_temp)
    print("Los Angeles Average Max Temp: ", los_angeles_aveg_max_temp)
    print("Boise Average Max Temp: ", boise_aveg_max_temp)
