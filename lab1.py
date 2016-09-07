import requests

#returns the status code response = requests.get('http://www.google.ca')
#response = requests.post('http://ccid-eddieantonio.rhcloud.com/makepeac')
response = requests.get("https://raw.githubusercontent.com/sensible-heart/CMPUT404Lab1/master/lab1.py")
print response.text