import requests
import json

url = "http://127.0.0.1:8001/arduino_info/"
url2 = "http://127.0.0.1:8001/output/"

data = {
    "battery": 0,
    "battery_tem": "25",
    "waringsign_status": 2,
    "UltraSound": "1"
}

headers = {
    "Content-Type": "application/json"
}

# 打印送出的資料並說明各資料型態
print("送出的資料:")
for key, value in data.items():
    value_type = "數字" if isinstance(value, int) else "字串"
    print(f"{key}: {value} ({value_type})")

# 發送 POST 請求
print("\nSend Data")
response = requests.post(url, data=json.dumps(data), headers=headers)
print("伺服器回應狀態碼:", response.status_code)
print("伺服器回應內容:", response.json())

# 發送 GET 請求
print("\nArduino Output")
response2 = requests.get(url2, data=json.dumps(data), headers=headers)
print("伺服器回應狀態碼:", response2.status_code)
print("伺服器回應內容:", response2.json())
