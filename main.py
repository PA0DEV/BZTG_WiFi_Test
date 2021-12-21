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

with open("settings.json") as f:
    settings = json.load(f)

ssid = settings["wifi"]["ssid"]
password = settings["wifi"]["pass"]
print(ssid)
print(password)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print(".")
        time.sleep(0.5)
        ...

print('network config:', wlan.ifconfig())

while True:
    ...



