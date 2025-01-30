# project-cli-weather-application-

Weather Fetcher

A simple Python script that fetches the current weather information for a given city or state using the OpenWeatherMap API.
Features
    • Fetches weather conditions for any city/state entered by the user. 
    • Displays the weather description and temperature. 

Prerequisites
    • Python 3.x installed on your system. 
    • An active internet connection. 
    • A valid API key from OpenWeatherMap (Replace the existing API key with your own for security reasons). 

Installation & Usage
   
    1. Clone this repository:
       git clone https://github.com/yourusername/weather-fetcher.git
       cd weather-fetcher
   
    2. Install dependencies (if required):
       pip install requests
   
    3. Run the script:
       python weather.py
   
    4. Enter the name of the city/state when prompted.

Example Output
Enter city/state name: London
current weather in London:
Clear - clear sky
temperature is: 15.85 C

API Key Security
This script currently contains a hardcoded API key. For better security:
    • Obtain your own API key from OpenWeatherMap. 
    • Store it in an environment variable or a configuration file instead of hardcoding it. 

License
This project is licensed under the MIT License.

Contribution
Feel free to fork this repository and contribute by submitting a pull request!

Author
Himanshu
