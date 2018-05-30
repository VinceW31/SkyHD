import os
import time
import datetime
import skybox_ip
import SkyChannelList
import requests
import urllib3
from flask import Flask, redirect, request, url_for

IP = (str(skybox_ip.ip1) + "." + str(skybox_ip.ip2) + "." + str(skybox_ip.ip3) + "." + str(skybox_ip.ip4))
print("SkyBox IP = ",IP)

try:
    os.system ("sudo /usr/local/bin/noip2")
except:
    print("Unable to start No-ip DUC service")

now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
Vol_Range = 1
delay = 0.5000
http = urllib3.PoolManager()
#lamp_ON = 'http://192.168.1.95/control?cmd=gpio,12,1'
#lamp_OFF = 'http://192.168.1.95/control?cmd=gpio,12,0'
lamp_ON = 'http://192.168.1.95/on'
lamp_OFF = 'http://192.168.1.95/off'

app = Flask(__name__)

def find_character_code_sequence(char): #this is for the Search function
    if char == "a":
        character_code_sequence = " 2"
    elif char == "b":
        character_code_sequence = " 2 2"
    elif char == "c":
        character_code_sequence = " 2 2 2"
    elif char == "d":
        character_code_sequence = " 3"
    elif char == "e":
        character_code_sequence = " 3 3"
    elif char == "f":
        character_code_sequence = " 3 3 3"
    elif char == "g":
        character_code_sequence = " 4"
    elif char == "h":
        character_code_sequence = " 4 4"
    elif char == "i":
        character_code_sequence = " 4 4 4"
    elif char == "j":
        character_code_sequence = " 5"
    elif char == "k":
        character_code_sequence = " 5 5"
    elif char == "l":
        character_code_sequence = " 5 5 5"
    elif char == "m":
        character_code_sequence = " 6"
    elif char == "n":
        character_code_sequence = " 6 6"
    elif char == "o":
        character_code_sequence = " 6 6 6"
    elif char == "p":
        character_code_sequence = " 7"
    elif char == "q":
        character_code_sequence = " 7 7"
    elif char == "r":
        character_code_sequence = " 7 7 7"
    elif char == "s":
        character_code_sequence = " 7 7 7 7"
    elif char == "t":
        character_code_sequence = " 8"
    elif char == "u":
        character_code_sequence = " 8 8"
    elif char == "v":
        character_code_sequence = " 8 8 8"
    elif char == "w":
        character_code_sequence = " 9"
    elif char == "x":
        character_code_sequence = " 9 9"
    elif char == "y":
        character_code_sequence = " 9 9 9"
    elif char == "z":
        character_code_sequence = " 9 9 9 9"
    elif char == " ":
        character_code_sequence = " 0"
    elif char == "1":
        character_code_sequence = " 1 1 1 1 1 1"
    elif char == "2":
        character_code_sequence = " 2 2 2 2"
    elif char == "3":
        character_code_sequence = " 3 3 3 3"
    elif char == "4":
        character_code_sequence = " 4 4 4 4"
    elif char == "5":
        character_code_sequence = " 5 5 5 5"
    elif char == "6":
        character_code_sequence = " 6 6 6 6"
    elif char == "7":
        character_code_sequence = " 7 7 7 7 7"
    elif char == "8":
        character_code_sequence = " 8 8 8 8"
    elif char == "9":
        character_code_sequence = " 9 9 9 9 9"
    elif char == "0":
        character_code_sequence = " 0 0"
    elif char == ".":
        character_code_sequence = " 1"
    elif char == ",":
        character_code_sequence = " 1 1"
    elif char == ";":
        character_code_sequence = " 1 1 1"
    elif char == ":":
        character_code_sequence = " 1 1 1 1"
    elif char == "'":
        character_code_sequence = " 1 1 1 1 1"
    return character_code_sequence

def log_channel(phrase, IP, channel):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nSkyHD box IP: " + IP + "\nChannel: " + channel)
        f.close()

def log_action(phrase, IP, action):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nSkyHD box IP: " + IP + "\nAction: " + action)
        f.close()

def log_IR(phrase, action):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nAction: " + action)
        f.close()

def log_device(phrase, action, result):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nAction: " + action + "\nResult: " + result)
        f.close()

@app.route("/<phrase>", methods = ['POST', 'GET'])
       
def data_input(phrase):
    print("Command recieved is " + phrase)
    phrase = phrase.lower().strip()
    print("Revised command is " + phrase)
    
#Devices Control
    if "switchdevice" in phrase:
        if "lamp" in phrase:
            if "on" in phrase:
                action = lamp_ON
                try:
                    r = http.request('GET', action)
                    r.status
                    if r.status == 200:
                        print(action)
                        print("Lamp is ON")
                        log_device(phrase, action, " Successful")
                except:
                    print("Failed to establish connection")
                    log_device(phrase, action, " Fail")
                    
            elif "off" in phrase:
                #command = "Switch the Lamp OFF"
                action = lamp_OFF
                try:
                    r = http.request('GET', action)
                    r.status
                    if r.status == 200:
                        print(action)
                        print("Lamp is OFF")
                        log_device(phrase, action, " Successful")
                except:
                    print("Failed to establish connection")
                    log_device(phrase, action, " Fail")
        phrase = phrase + "channels" #do not delete, needed for "Switch the TV.... commands"
    
# TV control (IR Functions, if BlackBean RM3 is used)
    if "tvir" in phrase:
        if " mute" in phrase or " unmute" in phrase:
            #os.system ("python RM3control.py -c mute")
            os.system ("python BlackBeanControl.py -c mute")
            log_IR(phrase," TV Volume Mute/Unmute")

        elif " on" in phrase or " off" in phrase:
           # os.system ("python RM3control.py -c power" )
            os.system ("python BlackBeanControl.py -c power" )
            log_IR(phrase," TV Power ON/OFF")

        elif " up" in phrase:
            for i in range (Vol_Range):
                #os.system ("python RM3control.py -c volup")
                os.system ("python BlackBeanControl.py -c volup")
                log_IR(phrase," TV Volume UP")
                time.sleep(.500)

        elif " down" in phrase:
            for i in range (Vol_Range):
                #os.system ("python RM3control.py -c voldown")
                os.system ("python BlackBeanControl.py -c voldown")
                log_IR(phrase," TV Volume DOWN")
                time.sleep(.500)
  
# menus (show, go to, whats on, ip/menus "text")

    if "menus" in phrase:
        if "tv guide" in phrase or "tvguide" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select")
            log_action(phrase,IP," navigate to TV Guide Menu")
            
        if "planner" in phrase or "planet" in phrase : 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " down" + " select")
            log_action(phrase,IP," navigate to Planner Menu")
            
        if "catch up" in phrase or "catchup" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " right" + " select")
            log_action(phrase,IP," navigate to Catch Up Menu")
            
        if "movies" in phrase or "films" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right" + " right" + " right" + " right")
            log_action(phrase,IP," navigate to Movies Menu")
            
        if "documentaries" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right" + " right")
            log_action(phrase,IP," navigate to Documentaries Menu")
            
        if "favourites" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " left")
            log_action(phrase,IP," navigate to Favourites Menu")
            
        if "plus 1" in phrase or "plus one" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right")
            log_action(phrase,IP," navigate to +1 Menu")
            
        if "next page" in phrase:
            os.system ("sky-remote-cli " + IP + " channeldown")
            log_action(phrase,IP," navigate to Next Page")

        if "last page" in phrase or "back page" in phrase or "go back a page" in phrase:
            os.system ("sky-remote-cli " + IP + " channelup")
            log_action(phrase,IP," navigate to Previous Page")
            
        if "backup" in phrase or "back up" in phrase:
            os.system ("sky-remote-cli " + IP + " backup")
            log_action(phrase,IP," backup button")

# Return to programme (return to, go back to)

    if "skybutton" in phrase:  
        os.system ("sky-remote-cli " + IP + " sky")
        log_action(phrase,IP," sky button")

# Recording (record programme, record this programme, record series)

    if "record" in phrase:
        if "programme" in phrase or "program" in phrase:
            os.system ("sky-remote-cli " + IP + " record" + " record" + " select")
            log_action(phrase,IP," record program")
        elif "series" in phrase:
            os.system ("sky-remote-cli " + IP + " record" + " record" + " down" + " select")
            log_action(phrase,IP," record series")
            
# Channel names (Switch to, change to, show, TV to, whats on, watch)

    if "channels" in phrase: 
        
        if "sky news" in phrase:
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.skynews)
            log_channel(phrase,IP,SkyChannelList.skynews)

        if "discovery" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.discovery)
            log_channel(phrase,IP,SkyChannelList.discovery)
            
        if "gold" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.gold)
            log_channel(phrase,IP,SkyChannelList.gold)
            
        if "dave" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.dave)
            log_channel(phrase,IP,SkyChannelList.dave)
            
        if "tlc" in phrase or "t l c" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.tlc)
            log_channel(phrase,IP,SkyChannelList.tlc)
            
        if "alibi" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.alibi)
            log_channel(phrase,IP,SkyChannelList.alibi)
            
        if "f1" in phrase or "f 1" in phrase or "f one" in phrase or "formula 1" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.f1)
            log_channel(phrase,IP,SkyChannelList.f1)
            
        if "atlantic" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.atlantic)
            log_channel(phrase,IP,SkyChannelList.atlantic)
            
        if "universal" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.universal)
            log_channel(phrase,IP,SkyChannelList.universal)
            
        if "national geographic" in phrase or "nat geo" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.nat_geo)
            log_channel(phrase,IP,SkyChannelList.nat_geo)
            
        if "sky 1" in phrase or "sky one" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.sky_1)          
            log_channel(phrase,IP,SkyChannelList.sky_1)
            
        if "channel 4" in phrase or "channel four" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_4)
            log_channel(phrase,IP,SkyChannelList.ch_4)

        if "channel 5" in phrase or "channel five" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_5)
            log_channel(phrase,IP,SkyChannelList.ch_5)
            
        if "bbc" in phrase: 
            if "bbc 1" in phrase or "bbc one" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_1)
                log_channel(phrase,IP,SkyChannelList.bbc_1)
            elif "bbc 2" in phrase or "bbc to" in phrase or "bbc too" in phrase or "bbc two" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_2)
                log_channel(phrase,IP,SkyChannelList.bbc_2)
            elif "bbc 4" in phrase or "bbc four" in phrase:  
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_4)
                log_channel(phrase,IP,SkyChannelList.bbc_4)
            elif "bbc local" in phrase or "bbc bristol" in phrase or "bbc south west" in phrase or "bbc west" in phrase:
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_local)
                log_channel(phrase,IP,SkyChannelList.bbc_local)
            else:
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.skynews)
                log_channel(phrase,IP,SkyChannelList.skynews)


        if "itv" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.itv_1)
            log_channel(phrase,IP,SkyChannelList.itv_1)

        if "channels to channel" in phrase or "channels channel to" in phrase or "number" in phrase:
            print("phrase is " + phrase)
            if "channel 4" in phrase or "channel four" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_4)
                log_channel(phrase,IP,SkyChannelList.ch_4)
            elif "channel 5" in phrase or "channel five" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_5)
                log_channel(phrase,IP,SkyChannelList.ch_5)
            else:
                print("channel number detected in phrase?")
                word_list = phrase.split()
                if word_list[2].isnumeric():
                    a = 2 # numeric element of string starts at word "a"
                elif word_list[3].isnumeric():
                    a = 3
                elif word_list[4].isnumeric():
                    a = 4
                    
                if word_list[a].isnumeric():
                    print("Channel number recieved is numerical")
                    number = word_list[a]                 
                    if len(word_list[a]) > 1:
                        print("Channel number recieved is in format (nnn)")
                        channel_number = number[0] + " " + number[1] + " " + number[2]
                        print("Channel number modified to " + channel_number)
                    else:
                        print("Channel number recieved is in format (n n n)")
                        channel_number = word_list[a] + " " + word_list[a+1] + " " + word_list[a+2]
                        print("Channel number modified to " + channel_number)
                os.system ("sky-remote-cli " + IP + " sky"  + " " + channel_number)
                log_channel(phrase,IP,channel_number)
                print("Sending - sky," + channel_number)
# play/pause etc (pause tv, pause programme, continue)
    if "pause" in phrase: 
        os.system ("sky-remote-cli " + IP + " pause")
        log_action(phrase,IP," pause")
        print("Sending - pause")
    if "continue" in phrase: 
        os.system ("sky-remote-cli " + IP + " play")
        log_action(phrase,IP," play")
        print("Sending - play")

# Search for programmes
    if "search" in phrase:
        my_str = phrase
        word_list = my_str.split()
        n = (len(phrase.split()))
        print("search term is ", n-1, "words long")
        search_string = phrase.split(' ',1)[1]
        print(search_string)
        string_length = len(search_string)
    # navigate to search box
        os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " up")
        print("Sending - sky, tvguide, up")
    # send search string to search box
        for i in range(string_length):
            character = search_string[i]
            character_code = find_character_code_sequence(search_string[i])
            os.system ("sky-remote-cli " + IP + character_code)
            print("Sending - " + character_code)
            time.sleep(.500) # do no tmake this less than 500 m/sec
        log_action(phrase,IP,search_string)      
    return "OK" # this is just there to stop browser error reports due to no response

if __name__== "__main__":
    app.run(host='0.0.0.0' , debug=False, use_reloader=False)


