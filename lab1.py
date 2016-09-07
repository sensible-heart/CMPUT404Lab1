import requests

#returns the status code response = requests.get('http://www.google.ca')
response = requests.post('http://ccid-eddieantonio.rhcloud.com/makepeac')
print response.status_code