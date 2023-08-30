import requests
from time import sleep

url = "http://192.168.137.239/"
for i in range(5):
    requests.get(url + "on")
    sleep(0.2)
    requests.get(url + "off")
    sleep(0.2)
