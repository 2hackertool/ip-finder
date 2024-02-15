#ip finder
import socket as s
print(''' _          __ _           _
(_)_ __    / _(_)_ __   __| | ___ _ __
| | '_ \  | |_| | '_ \ / _` |/ _ \ '__|
| | |_) | |  _| | | | | (_| |  __/ |
|_| .__/  |_| |_|_| |_|\__,_|\___|_|
  |_| ''')
print("note dont type http or https type like www.bing.com or bing.com")
print("you can find any website ip adders")
print("tool made by hackertool")
try:
    host = input('Enter the url of the website : ')
    print(f'IP of {host} is {s.gethostbyname(host)}')
except Exception as e:
    print('Failed to resolve IP: ', e)
