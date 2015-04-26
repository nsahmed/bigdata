__author__ = 'Nishat'


import urllib
import json

enigma_api= "6336800936fe4cd1fd565f4865f4e792"

temp_url = 'https://api.enigma.io/v2/data/6336800936fe4cd1fd565f4865f4e792/us.gov.dot.rita.trans-stats.on-time-performance.2009?page=';
n= 6;
for i in range(1,n):
    print i;
    url = temp_url + str(i);
    print url;
    json_obj = urllib.urlopen(url);
    url = "";
    json_str = json_obj.read().decode('utf-8');
    data = json.loads(json_str);

    urllib.urlcleanup();

    #for item in data['result']:
    try:
       print i;
       #Open a json file for writing
       file = open("C:/Users/Nishat/Desktop/FlightData.json","a")

       #write data to file
       json.dump(data,file,indent=4);

       #close a file
       file.close();

    except IOError as e:
       print("Exception caught: ({})".format(e))

    print("Loop iteration: " + str(i));

print("Data is saved to FlightData.json file!")
