import requests

url = 'http://127.0.0.1:8000/api/v1/hospitals/?'

city = 'Lucknow'

url = url + 'city=' + city

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
data = response.json()

print(data[0]['name'])
print(data[0]['address'])
print(len(data))

count = 0
res = ''
for d in data: 
    name = d['name']
    address = d['address']
    count+=1
    res = res + str(count)+ '.Name:' + name + '\n' + 'Address:' + address + '\n'

print(res)