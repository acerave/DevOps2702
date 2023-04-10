import requests
response = requests.post("172.0.0.1:5001/whatismyname")
print(response.text)