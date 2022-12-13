import requests

lat=59.94
lon=30.31
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

responce = requests.get(url)
data = responce.json()
# print(data)
for key in data.keys():
    print(key, data[key])


n = 59.689457

print('{:.2f}'.format(n))
