# MetaWeather-API-Cities-Average-Maximum-Temperature-M
MetaWeather API repository
## Overview
Using the MetaWeather API ( https://www.metaweather.com/api/)  to find the average max temperature in Salt Lake City, Los Angeles, and Boise for a 6 day forecast
in python,  The code  makes requests concurrently  of each of the 3 API. 
## Details
The URLs to get temperatures for the 3 cities are:
Salt Lake City: https://www.metaweather.com/api/location/2487610/
Los Angeles: https://www.metaweather.com/api/location/2442047/
Boise: https://www.metaweather.com/api/location/2366355/
According to the MetaWeather API each one of these API calls will return a field called "consolidated_weather". It contains a weather forecast for the city for each day including today and the next 5 days. Each forecast includes a field called "max_temp" that is the max temperature for that forecasted day. 
## Output
A simple display of  each city with the calculated average max_temp.
