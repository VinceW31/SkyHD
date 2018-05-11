import os
import time
import skybox_ip
import SkyChannelList
from flask import Flask, redirect, request, url_for

IP = (str(skybox_ip.ip1) + "." + str(skybox_ip.ip2) + "." + str(skybox_ip.ip3) + "." + str(skybox_ip.ip4))
print("SkyBox IP = ",IP)

try:
    os.system ("sudo /usr/local/bin/noip2")
except:
    print("Unable to start No-ip DUC service")
    
Vol_Range = 1
delay = 0.5000

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

@app.route("/<phrase>", methods = ['POST', 'GET'])
       
def data_input(phrase):
    print("Command recieved is " + phrase)
    phrase = phrase.lower().strip()
    print("Revised command is " + phrase)

# TV control (IR Functions, if BlackBean RM3 is used)
    if "tvir" in phrase:
        if " mute" in phrase or " unmute" in phrase:
            os.system ("python BlackBeanControl.py -c mute")

        elif " on" in phrase or " off" in phrase:
            os.system ("python BlackBeanControl.py -c power" )

        elif " up" in phrase:
            for i in range (Vol_Range):
                os.system ("python BlackBeanControl.py -c volup")
                time.sleep(.500)

        elif " down" in phrase:
            for i in range (Vol_Range):
                os.system ("python BlackBeanControl.py -c voldown")
                time.sleep(.500)

    
# menus (show, go to, whats on, ip/menus "text")

    if "menus" in phrase:
        if "tv guide" in phrase or "tvguide" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select")

        if "planner" in phrase or "planet" in phrase : 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " down" + " select")

        if "catch up" in phrase or "catchup" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " right" + " select")

        if "movies" in phrase or "films" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right" + " right" + " right" + " right")
            
        if "documentaries" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right" + " right")

        if "favourites" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " left")
            
        if "plus 1" in phrase or "plus one" in phrase: 
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select" + " right" + " right")

        if "next page" in phrase:
            os.system ("sky-remote-cli " + IP + " channeldown")

        if "last page" in phrase or "back page" in phrase or "go back a page" in phrase:
            os.system ("sky-remote-cli " + IP + " channelup")
            
        if "backup" in phrase or "back up" in phrase:
            os.system ("sky-remote-cli " + IP + " backup")

# Return to programme (return to, go back to)

    if "skybutton" in phrase:  
        os.system ("sky-remote-cli " + IP + " sky")

# Recording (record programme, record this programme, record series)

    if "record" in phrase:
        if "programme" in phrase or "program" in phrase:
            os.system ("sky-remote-cli " + IP + " record" + " record" + " select")
        elif "series" in phrase:
            os.system ("sky-remote-cli " + IP + " record" + " record" + " down" + " select")
            
# Channel names (Switch to, change to, show, TV to, whats on, watch)

    if "channels" in phrase: 
        
        if "sky news" in phrase:
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.skynews)

        if "discovery" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.discovery)

        if "gold" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.gold)

        if "dave" in phrase: 
             os.system ("sky-remote-cli " + IP + " " + SkyChannelList.dave)

        if "tlc" in phrase or "t l c" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.tlc)

        if "alibi" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.alibi)
            
        if "f1" in phrase or "f 1" in phrase or "f one" in phrase or "Formula 1" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.f1)

        if "atlantic" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.atlantic)

        if "universal" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.universal)

        if "national geographic" in phrase or "nat geo" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.nat_geo)

        if "sky 1" in phrase or "sky one" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.sky_1)          


        if "bbc" in phrase: 
            if "bbc 1" in phrase or "bbc one" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_1)
            elif "bbc 2" in phrase or "bbc to" in phrase or "bbc too" in phrase or "bbc two" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_2)
            elif "bbc 4" in phrase or "bbc four" in phrase:  
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_4)
            elif "bbc local" in phrase or "bbc bristol" in phrase or "bbc south west" in phrase or "bbc west" in phrase:
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_local)
            else:
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.skynews)


        if "itv" in phrase: 
            os.system ("sky-remote-cli " + IP + " " + SkyChannelList.itv_1)

        if "channels to channel" in phrase or "channels channel to" in phrase:
            print("phrase is " + phrase)
            if "channel 4" in phrase or "channel four" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_4)
            elif "channel 5" in phrase or "channel five" in phrase: 
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.ch_5)
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
                print("Sending - sky," + channel_number)

# play/pause etc (pause tv, pause programme, continue)
    if "pause" in phrase: 
        os.system ("sky-remote-cli " + IP + " pause")
        print("Sending - pause")
    if "continue" in phrase: 
        os.system ("sky-remote-cli " + IP + " play")
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
               
    return "OK" # this is just there to stop browser error reports due to no response

if __name__== "__main__":
    app.run(host='0.0.0.0' , debug=False, use_reloader=False)


