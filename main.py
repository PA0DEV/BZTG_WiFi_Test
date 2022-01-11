#
# name: Phillip Ahlers 
# created:  21.12.2021
# class: ETS2021
#
#
# use:
# 
# 
# version: 2021_12_21_XXX
# designed and tested on ESP32 TTGO whith XXX
# pin conenctions:
# 
# 
# used external libaries:
# 
# ----------------------------------------
#

import network
import json
import time
import usocket as socket

var = 12.02


# Load settings
with open("settings.json") as f:
    settings = json.load(f)
stMode = settings["wifi"]["stMode"]
apMode = settings["wifi"]["apMode"]

wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

# start connection to AP from settings.json
if stMode:
    ssid = settings["wifi"]["ssid"]
    password = settings["wifi"]["pass"]
    
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to ', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            ## Wait for connection
            print(".", end="")
            time.sleep(0.5)
    print()
    print('network config:')
    print("Client IP: ",wlan.ifconfig()[0])
    print("Subnet:", wlan.ifconfig()[1])
    print("Gateway:", wlan.ifconfig()[2])
    print("DNS-server: ", wlan.ifconfig()[3])

#open AP if AP Mode
if apMode:
    APssid = settings["wifi"]["APssid"]
    APpassword = settings["wifi"]["APpass"]
    
    ap.active(True)
    ap.config(essid=APssid, authmode=network.AUTH_WPA_WPA2_PSK, password = APpassword)

    print()
    print('network config:')
    print("Server IP: ",ap.ifconfig()[0])
    print("Subnet:", ap.ifconfig()[1])
    print("Gateway:", ap.ifconfig()[2])
    print("DNS-server: ", ap.ifconfig()[3])

ap_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ap_socket.bind(('', 80))
ap_socket.listen(5)

print(ap.ifconfig())
print(wlan.ifconfig())



while True:
    con, adr = ap_socket.accept()
    print("Anfrage von IP-Adresse {0}".format(str(adr)))
    request = con.recv(1024)
    con.send('HTTP/1.1 200 OK\n')
    con.send('Content-Type: text/html\n')
    con.send('Connection: close\n\n')
    response = "<h1><span style=\"color: #ff0000;\"><strong>Hallo BZTG!" + str(var) +"</strong></span></h1>"
    con.sendall(response)
    con.close()



