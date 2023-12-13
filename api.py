import requests
url="https://emojihub.yurace.pro/api/random"
response=requests.get(url)
data=response.json()
print(data)