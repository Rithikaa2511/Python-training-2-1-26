import json

with open("jsonData.json",'r')as f:
    data = json.load(f)
    print(data)