import requests


url = "https://apis.openapi.sk.com/tmap/routes?version=3&format=json"
headers = {"appKey": "kyUPwz0Ly2aplTsQ72YKp2EjfDwbI0EJ9KFRwUA4"}
data = {
    "startX": 126.98446467,
    "startY": 37.57539772,
    "endX": 127.02493533,
    "endY": 37.50049048,
    "reqCoordType": "WGS84GEO",
    "resCoordType": "WGS84GEO",
    "searchOption": "0",
    "trafficInfo": "Y",
    "carType": 7,
    "totalValue": 2,
}
resp = requests.post(url, headers=headers, data=data).json()
print(resp)
eta = resp["features"][0]["properties"]["totalTime"] // 60

print(resp["features"][0]["properties"]["totalTime"] // 60)
print(eta)
