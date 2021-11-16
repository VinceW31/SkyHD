import os
import time
import datetime
import threading
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

CarCharger_Start_Time_Hours = 21
CarCharger_Stop_Time_Hours = 7
CarChargerStatus = 0

Dishwasher_Start_Time_Hours = 21
DishwasherStatus = 0

Xmas_Lights_Start_Time_Hours = 16
Xmas_Lights_Start_Time_Min = 30
Xmas_Lights_Stop_Time_Hours = 23
Xmas_Lights_Stop_Time_Min = 00
Xmas_Lights_Show_Time1_Hours = 17 #first show
Xmas_Lights_Show_Time1_Min = 00
Xmas_Lights_Show_Time2_Hours = 19 #second show
Xmas_Lights_Show_Time2_Min = 00
Xmas_Lights_Status = 0 
Porch_Light_Start_Time_Hours = 16
Porch_Light_Start_Time_Minutes = 45
Porch_Light_Stop_Time_Hours = 0
Porch_Light_Stop_Time_Minutes = 0
Porch_Light_Status = 0
Watering_Plants_Status = 0
Watering_Start_Time_Hours = 13
Watering_Start_Time_Minutes = 1
Show_Status = 0
Show_Duration = 4

Watering_Calendar = 0 # 1 for ON, 0 for OFF
WateringTime = 1 # Number of minutes to water the flowers 
activate_xmas_lights = 0 #Switch this to 1 if you want the Xmas lights to come on


now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
Hour = datetime.datetime.now().strftime('%H')
Minute = datetime.datetime.now().strftime('%M')
Day = datetime.datetime.now().strftime('%d')
Month = datetime.datetime.now().strftime('%m')
CurrentHour = int(Hour)
CurrentMinute = int(Minute)
CurrentDay = int(Day)
CurrentMonth = int(Month)

Vol_Range = 1
delay = 0.5000
http = urllib3.PoolManager()
tap = 0

lamp_ON = 'http://192.168.1.121/on'
lamp_OFF = 'http://192.168.1.121/off'
kitchen_lights_ON = 'http://192.168.1.118/on'
kitchen_lights_OFF = 'http://192.168.1.118/off'
lounge_lights_ON = 'http://192.168.1.119/on'
lounge_lights_OFF = 'http://192.168.1.119/off'
diningroom_lights_ON = 'http://192.168.1.120/on'
diningroom_lights_OFF = 'http://192.168.1.120/off'
outside_xmas_lights_ON = 'http://192.168.1.126/on'
outside_xmas_lights_OFF = 'http://192.168.1.126/off'
outside_xmas_lights_CYCLE = 'http://192.168.1.126/cycle'
xmas_lights_controller_ON = 'http://192.168.1.134/on'
xmas_lights_controller_OFF = 'http://192.168.1.134/off'
xmas_lights_controller_CYCLE = 'http://192.168.1.134/cycle'
back_xmas_lights_ON = 'http://192.168.1.180/on'
back_xmas_lights_OFF = 'http://192.168.1.180/off'
bed1_xmas_lights_ON = 'http://192.168.1.128/on'
bed1_xmas_lights_OFF = 'http://192.168.1.128/off'
bed2_xmas_lights_ON = 'http://192.168.1.133/on' 
bed2_xmas_lights_OFF = 'http://192.168.1.133/off' 
hall_xmas_lights_ON = 'http://192.168.1.138/on'
hall_xmas_lights_OFF = 'http://192.168.1.138/off'
diningroom_xmas_lights_ON = 'http://192.168.1.132/on'
diningroom_xmas_lights_OFF = 'http://192.168.1.132/off'
lounge1_xmas_lights_ON = 'http://192.168.1.135/on'
lounge1_xmas_lights_OFF = 'http://192.168.1.135/off'
lounge2_xmas_lights_ON = 'http://192.168.1.136/on'
lounge2_xmas_lights_OFF = 'http://192.168.1.136/off'
conservatory_xmas_lights_ON = 'http://192.168.1.114/on'
conservatory_xmas_lights_OFF = 'http://192.168.1.114/off'
conservatory_lights_ON = 'http://192.168.1.137/on'
conservatory_lights_OFF = 'http://192.168.1.137/off'
conservatory_lights_TOGGLE = 'http://192.168.1.137/toggle'
floodlight_ON = 'http://192.168.1.180/on'
floodlight_OFF = 'http://192.168.1.180/off'
outside_lights_ON = 'http://192.168.1.101/on'
outside_lights_OFF = 'http://192.168.1.101/off'
outside_lights_TOGGLE = 'http://192.168.1.101/toggle'
outside_tap_ON = 'http://192.168.1.113/on'
outside_tap_OFF = 'http://192.168.1.113/off'
CarCharger_ON = 'http://192.168.1.228/on'
CarCharger_OFF = 'http://192.168.1.228/off'
Dishwasher_ON = 'http://192.168.1.122/on'
Dishwasher_OFF = 'http://192.168.1.122/off'
Printer_ON = 'http://192.168.1.64/on'
Printer_OFF = 'http://192.168.1.64/off'
Porch_Light_ON = 'http://192.168.1.155/on'
Porch_Light_OFF = 'http://192.168.1.155/off'

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
    #with open("log.txt", "a") as f:
        #f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nSkyHD box IP: " + IP + "\nChannel: " + channel)
        #f.close()

def log_action(phrase, IP, action):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    #with open("log.txt", "a") as f:
        #f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nSkyHD box IP: " + IP + "\nAction: " + action)
        #f.close()

def log_IR(phrase, action):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    #with open("log.txt", "a") as f:
        #f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nAction: " + action)
        #f.close()

def log_device(phrase, action, result):
    now = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
    #with open("log.txt", "a") as f:
        #f.write("\n\n" + now + "\nPhrase recieved = " + phrase + "\nAction: " + action + "\nResult: " + result)
        #f.close()

def switch_device(phrase, device_action):    
    try:
        r = http.request('GET', device_action)
        r.status
        if r.status == 200:
            print(device_action, " Successful")
            log_device(phrase, device_action, " Successful")
        else:
            print(device_action, " Invalid Status reply from device")
            log_device(phrase, device_action, " Invalid Status reply from device")   
    except:
        print(device_action, " Fail")
        log_device(phrase, device_action, " Fail")    

def water_the_plants(sec):
    print("Watering the flowers for 60 seconds")
    time.sleep(sec)
    action = outside_tap_OFF
    phrase = "outside tap (after auto delay)"
    switch_device(phrase, action)
    print("Watering turned OFF")

# Timer functions ***************

def CarChargerTimer_ON():
    global CarChargerStatus
    print("Switching the CarCharger ON (timer function)")
    action = CarCharger_ON
    phrase = "Car Charger ON (timer function)"
    switch_device(phrase, action)
    print("Car Charger ON (timer function)")
    CarChargerStatus = 1

def CarChargerTimer_OFF():
    global CarChargerStatus
    print("Switching the CarCharger OFF (timer function)")
    action = CarCharger_OFF
    phrase = "Car Charger OFF (timer function)"
    switch_device(phrase, action)
    print("Car Charger OFF (timer function)")
    CarChargerStatus = 0

def Xmas_Lights_ON():
    global Xmas_Lights_Status
    print("Switching the Xmas Lights ON (timer function)")
    phrase = "Xmas Lights ON (timer function)"
    switch_device(phrase, bed1_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, bed2_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, lounge1_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, lounge2_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, diningroom_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, conservatory_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, hall_xmas_lights_ON)
    time.sleep(0.5)
    switch_device(phrase, back_xmas_lights_ON)
    time.sleep(1.5)
    switch_device(phrase, outside_xmas_lights_CYCLE)
    time.sleep(2)
    switch_device(phrase, xmas_lights_controller_CYCLE)
    Xmas_Lights_Status = 1
    
def Xmas_Lights_OFF():
    global Xmas_Lights_Status
    print("Switching the Xmas Lights OFF (timer function)")
    phrase = "Xmas Lights OFF (timer function)"
    switch_device(phrase, xmas_lights_controller_OFF)
    time.sleep(0.5)
    switch_device(phrase, outside_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, bed1_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, bed2_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, lounge1_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, lounge2_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, diningroom_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, conservatory_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, hall_xmas_lights_OFF)
    time.sleep(0.5)
    switch_device(phrase, back_xmas_lights_OFF)
    Xmas_Lights_Status = 0

def Xmas_Lights_Music_Show():
    global Xmas_Lights_Status
    print("Switching on the Xmas Lights Music Show (timer function)")
    phrase = "Xmas Lights Music Show (timer function)"
    switch_device(phrase, xmas_lights_controller_OFF)
    time.sleep(1)
    switch_device(phrase, outside_xmas_lights_OFF)
    time.sleep(5)
    switch_device(phrase, outside_xmas_lights_ON)
    time.sleep(2)
    switch_device(phrase, xmas_lights_controller_ON)
    Xmas_Lights_Status = 1

def gettime():
    global CurrentMinute
    global CurrentHour
    global CurrentMonth
    global CurrentDayofWeek
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Hour = datetime.datetime.now().strftime('%H')
    Minute = datetime.datetime.now().strftime('%M')
    Day = datetime.datetime.now().strftime('%d')
    DayofWeek = datetime.datetime.now().strftime('%u')
    Month = datetime.datetime.now().strftime('%m')    
    CurrentHour = int(Hour)
    CurrentMinute = int(Minute)
    CurrentDay = int(Day)
    CurrentMonth = int(Month)
    CurrentDayofWeek = int(DayofWeek)
    get_Porch_Light_Start_Time()
    print(now)
    print " "

def get_Porch_Light_Start_Time():
    global CurrentMonth
    global Porch_Light_Start_Time_Hours
    global Porch_Light_Start_Time_Minutes
    if CurrentMonth == 1:
        Porch_Light_Start_Time_Hours = 16
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 2:
        Porch_Light_Start_Time_Hours = 16
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 3:
        Porch_Light_Start_Time_Hours = 18
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 4:
        Porch_Light_Start_Time_Hours = 18
        Porch_Light_Start_Time_Minutes = 30
    elif CurrentMonth == 5:
        Porch_Light_Start_Time_Hours = 19
        Porch_Light_Start_Time_Minutes = 20
    elif CurrentMonth == 6:
        Porch_Light_Start_Time_Hours = 20
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 7:
        Porch_Light_Start_Time_Hours = 20
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 8:
        Porch_Light_Start_Time_Hours = 19
        Porch_Light_Start_Time_Minutes = 15
    elif CurrentMonth == 9:
        Porch_Light_Start_Time_Hours = 18
        Porch_Light_Start_Time_Minutes = 40
    elif CurrentMonth == 10:
        Porch_Light_Start_Time_Hours = 16
        Porch_Light_Start_Time_Minutes = 40
    elif CurrentMonth == 11:
        Porch_Light_Start_Time_Hours = 16
        Porch_Light_Start_Time_Minutes = 0
    elif CurrentMonth == 12:
        Porch_Light_Start_Time_Hours = 16
        Porch_Light_Start_Time_Minutes = 0
    else:
        Porch_Light_Start_Time_Hours = 23
        Porch_Light_Start_Time_Minutes = 0
        print "Month not recognised"
    
class DailyTasksProg:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global CurrentMinute
        global CurrentHour
        global CurrentDay
        global CurrentDayofWeek
        global CarChargerTask 
        global CarChargerTask_Started 
        global CarCharger_Started_Day
        global CarChargerStatus
        global DishwasherStatus
        global Xmas_Lights_Status
        global Porch_Light_Status
        global Porch_Light_Start_Time_Hours
        global Porch_Light_Start_Time_Minutes
        global activate_xmas_lights
        global Show_Status
        global Watering_Plants_Status
        
        while self._running:
            gettime()
            print "Time Now is", datetime.datetime.now().strftime('%H:%M')
            print "Day of Week = ", CurrentDayofWeek
            print "Month = ", CurrentMonth
 
            #CarCharger*********************************
            if CurrentDayofWeek <=5: # if its Mon to Fri
                if CurrentHour >= CarCharger_Stop_Time_Hours: # if its past the OFF time
                    if CurrentHour < CarCharger_Start_Time_Hours: # but not past the ON time
                        if CarChargerStatus == 1: # and its status is ON
                            CarChargerTimer_OFF() # switch it OFF
                    else: # its past the ON time
                        if CarChargerStatus == 0: # if its status is OFF
                            CarChargerTimer_ON() # switch it ON
            else: # its a Sat or Sun
                if CarChargerStatus == 0: # if its status is OFF
                    CarChargerTimer_ON() # switch it ON 
            print "Car Charger Status = ", CarChargerStatus

            #Xmas Lights******************
            if activate_xmas_lights == 1:
                if Xmas_Lights_Status == 0:
                    if CurrentHour == Xmas_Lights_Start_Time_Hours:
                        if CurrentMinute >= Xmas_Lights_Start_Time_Min:
                            Xmas_Lights_ON()
                            Xmas_Lights_Status = 1

                if Xmas_Lights_Status == 1:
                    if CurrentHour == Xmas_Lights_Stop_Time_Hours:
                        if CurrentMinute >= Xmas_Lights_Stop_Time_Min:
                            Xmas_Lights_OFF()
                            Xmas_Lights_Status = 0
                print "Xmas Lights Status = ", Xmas_Lights_Status

            #Xmas Lights Music Show *****
            if activate_xmas_lights == 1:
                if Show_Status == 0:
                    if CurrentHour == Xmas_Lights_Show_Time2_Hours: #Second Show
                        if CurrentMinute == Xmas_Lights_Show_Time2_Min:
                            Xmas_Lights_Music_Show()
                            Show_Status = 1
                            Xmas_Lights_Status = 1
                    if CurrentHour == Xmas_Lights_Show_Time1_Hours: #First Show
                        if CurrentMinute == Xmas_Lights_Show_Time1_Min:
                            Xmas_Lights_Music_Show()
                            Show_Status = 1
                            Xmas_Lights_Status = 1

            if Show_Status == 1:
                if CurrentHour == Xmas_Lights_Show_Time1_Hours:
                    if CurrentMinute == Xmas_Lights_Show_Time1_Min + Show_Duration:
                        Show_Status = 0 #reset at the end of show 1
                if CurrentHour == Xmas_Lights_Show_Time2_Hours:
                    if CurrentMinute == Xmas_Lights_Show_Time2_Min + Show_Duration:
                        Show_Status = 0 #reset at the end of show 2
                        
            
            #Dishwasher******************
            if CurrentHour == Dishwasher_Start_Time_Hours:
                if DishwasherStatus == 0:
                    print("Switching the Dishwasher ON (timer function)")
                    
                    action = Dishwasher_ON
                    phrase = "Dishwasher ON (timer function)"
                    try:
                        r = http.request('GET', action)
                        r.status
                        if r.status == 200:
                            print(Dishwasher_ON)
                            log_device(phrase, action, " Successful")
                            DishwasherStatus = 1
                        else:
                            log_device(phrase, action, " Invalid Status reply from device")
                            DishwasherStatus = 0
                    except:
                        print("Failed to establish connection")
                        DishwasherStatus = 0
            else:
                DishwasherStatus = 0
            print "Dishwasher Status = ", DishwasherStatus

            #Porch Light*****************************
            if Porch_Light_Status == 0:
                if CurrentHour == Porch_Light_Start_Time_Hours:
                    if CurrentMinute >= Porch_Light_Start_Time_Minutes:
                        if activate_xmas_lights == 0:
                            print("Switching the Porch Light ON (timer function)")
                            action = Porch_Light_ON
                            phrase = "Porch Light ON (timer function)"
                            try:
                                r = http.request('GET', action)
                                r.status
                                if r.status == 200:
                                    print(Porch_Light_ON)
                                    log_device(phrase, action, " Successful")
                                    Porch_Light_Status = 1
                                else:
                                    log_device(phrase, action, " Invalid Status reply from device")
                                    Porch_Light_Status = 0
                            except:
                                print("Failed to establish connection")
                                Porch_Light_Status = 0
                        

            if Porch_Light_Status == 1:
                if CurrentHour == Porch_Light_Stop_Time_Hours:
                    if CurrentMinute >= Porch_Light_Stop_Time_Minutes:
                        print("Switching the Porch Light OFF (timer function)")
                        action = Porch_Light_OFF
                        phrase = "Porch Light OFF (timer function)"
                        try:
                            r = http.request('GET', action)
                            r.status
                            if r.status == 200:
                                print(Porch_Light_OFF)
                                log_device(phrase, action, " Successful")
                                Porch_Light_Status = 0
                            else:
                                log_device(phrase, action, " Invalid Status reply from device")
                                Porch_Light_Status = 1
                        except:
                            print("Failed to establish connection")
                            Porch_Light_Status = 1

                        
            print "Porch Light Status = ", Porch_Light_Status

            #Water the plants calendar basis*****************************
            if Watering_Plants_Status == 0:
                if CurrentHour == Watering_Start_Time_Hours:
                    if CurrentMinute == Watering_Start_Time_Minutes:
                        if Watering_Calendar == 1:
                            print("Watering the Flowers (timer function)")
                            watering_delay = 60*WateringTime 
                            action = outside_tap_ON
                            phrase = "Watering the Flowers (timer function)"
                            try:
                                r = http.request('GET', action)
                                r.status
                                if r.status == 200:
                                    print(outside_tap_ON)
                                    log_device(phrase, action, " Successful")
                                    Watering_Plants_Status = 1
                                else:
                                    log_device(phrase, action, " Invalid Status reply from device")
                                    Watering_Plants_Status = 0
                            except:
                                print("Failed to establish connection")
                                Watering_Plants_Status = 0
                        

            if Watering_Plants_Status == 1:
                #if CurrentHour >= Watering_Start_Time_Hours:
                if CurrentMinute >= Watering_Start_Time_Minutes + WateringTime:
                    print("Stop watering the flowers (timer function)")
                    action = outside_tap_OFF
                    phrase = "Stop watering the flowers (timer function)"
                    try:
                        r = http.request('GET', action)
                        r.status
                        if r.status == 200:
                            print(outside_tap_OFF)
                            log_device(phrase, action, " Successful")
                            Watering_Plants_Status = 0
                        else:
                            log_device(phrase, action, " Invalid Status reply from device")
                            Watering_Plants_Status = 1
                    except:
                        print("Failed to establish connection")
                        Watering_Plants_Status = 1

                        
            print "Watering Status = ", Watering_Plants_Status
            
            #End of timer section********************
            time.sleep(60) # run timer loop every 60 sec
                            
testThread = DailyTasksProg()
dailyTasksthread = threading.Thread(target = testThread.run)
dailyTasksthread.start()

# put all definitions before this line
@app.route("/<phrase>", methods = ['POST', 'GET'])
       
def data_input(phrase):
    global CarChargerTask 
    global CarChargerTask_Started 
    global CarCharger_Started_Day
    
    print("Command recieved is " + phrase)
    phrase = phrase.lower().strip()
    print("Revised command is " + phrase)

    
#Devices Control
    
    if "switchdevice" in phrase:
        if "kitchen" in phrase:
            if "lights" in phrase:
                if "on" in phrase:
                    action = kitchen_lights_ON
                if "off" in phrase:
                    action = kitchen_lights_OFF
                switch_device(phrase, action)
                
        if "lounge" in phrase:
            if "lights" in phrase or "light" in phrase:
                if "on" in phrase:
                    action = lounge_lights_ON
                if "off" in phrase:
                    action = lounge_lights_OFF
                switch_device(phrase, action)
            if "lamp" in phrase:
                if "on" in phrase:
                    action = lamp_ON
                if "off" in phrase:
                    action = lamp_OFF
                switch_device(phrase, action)

        if "dining room" in phrase:
            if "lights" in phrase or "light" in phrase:
                if "on" in phrase:
                    action = diningroom_lights_ON
                if "off" in phrase:
                    action = diningroom_lights_OFF
                switch_device(phrase, action)

        if "conservatory" in phrase:
            if "lights" in phrase or "light" in phrase:
                if "on" in phrase:
                    action = conservatory_lights_TOGGLE
                if "off" in phrase:
                    action = conservatory_lights_TOGGLE
                switch_device(phrase, action)
                
        if "flood light" in phrase or "garden light" in phrase :
            if "on" in phrase:
                action = floodlight_ON
            elif "off" in phrase:
                action = floodlight_OFF
            switch_device(phrase, action)
            
        if "outside lights" in phrase or "garden lights" in phrase :
            if "on" in phrase:
                action = outside_lights_TOGGLE
            elif "off" in phrase:
                action = outside_lights_TOGGLE
            switch_device(phrase, action)

        if "printer" in phrase :
            if "on" in phrase:
                action = Printer_ON
            elif "off" in phrase:
                action = Printer_OFF
            switch_device(phrase, action)
            
        if "test lamp" in phrase :
            if "on" in phrase:
                action = test_ON
            elif "off" in phrase:
                action = test_OFF
            switch_device(phrase, action)

        if "water" in phrase or "tap" in phrase :
            if "on" in phrase:
                action = outside_tap_ON 
            elif "off" in phrase:
                action = outside_tap_OFF
            switch_device(phrase, action)

        if "car charger" in phrase:
            if "on" in phrase:
                action = CarCharger_ON
                CarChargerTask_Started = 1
            elif "off" in phrase:
                action = CarCharger_OFF
                CarChargerTask_Started = 0
            switch_device(phrase, action)
            
        if "christmas lights" in phrase:
            if "outside" in phrase:
                if "on" in phrase:
                    switch_device(phrase, outside_xmas_lights_ON)
                elif "off" in phrase:
                    switch_device(phrase, outside_xmas_lights_OFF)
            else:
                if "on" in phrase:
                    Xmas_Lights_ON()
                elif "off" in phrase:
                    Xmas_Lights_OFF()

        if "all lights off" in phrase:
            switch_device(phrase, lamp_OFF)
            time.sleep(0.5)
            switch_device(phrase, floodlight_OFF)
            time.sleep(0.5)
            switch_device(phrase, diningroom_lights_OFF)
            time.sleep(0.5)
            switch_device(phrase, kitchen_lights_OFF)
            time.sleep(0.5)
            switch_device(phrase, lounge_lights_OFF)
            time.sleep(0.5)
                  
        if "tv" in phrase or "telly" in phrase:
            if " on" in phrase or " off" in phrase:
                os.system ("python /home/pi/SkyHD/BlackBeanControl.py -c power" )
                log_IR(phrase," TV Power ON/OFF")

        phrase = phrase + "channels" #do not delete, needed for "Switch the TV.... commands"

    if "watering" in phrase:
        if "flowers" in phrase or "plants" in phrase:
            watering_delay = 60*WateringTime 
            action = outside_tap_ON
            switch_device(phrase, action)
            wateringthread = threading.Thread(target = water_the_plants, args = [watering_delay])
            wateringthread.start()
                
# TV control (IR Functions)
    if "tvir" in phrase:
        if " mute" in phrase or " unmute" in phrase:
            os.system ("python /home/pi/SkyHD/BlackBeanControl.py -c mute")
            log_IR(phrase," TV Volume Mute/Unmute")

        elif " on" in phrase or " off" in phrase:
            os.system ("python /home/pi/SkyHD/BlackBeanControl.p -c power" )
            log_IR(phrase," TV Power ON/OFF")

        elif " up" in phrase:
            for i in range (Vol_Range):
                os.system ("python /home/pi/SkyHD/BlackBeanControl.py -c volup")
                log_IR(phrase," TV Volume UP")
                time.sleep(.500)

        elif " down" in phrase:
            for i in range (Vol_Range):
                os.system ("python /home/pi/SkyHD/BlackBeanControl.py -c voldown")
                log_IR(phrase," TV Volume DOWN")
                time.sleep(.500)
                
        elif " guide" in phrase:
            os.system ("sky-remote-cli " + IP + " sky" + " tvguide" + " select")
            log_action(phrase,IP," navigate to TV Guide Menu")
  
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
            
        if "gold" in phrase or "uk gold" in phrase: 
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
                os.system ("sky-remote-cli " + IP + " " + SkyChannelList.bbc_1)
                log_channel(phrase,IP,SkyChannelList.bbc_1)


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
            time.sleep(.500) # do not make this less than 500 m/sec
        log_action(phrase,IP,search_string)      
    return "OK" # this is just there to stop browser error reports due to no response

if __name__== "__main__":
    app.run(host='0.0.0.0' , debug=False, use_reloader=False)





