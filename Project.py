import pandas as pd
import math

data = pd.read_csv("Database.csv")
data["Temperature"] = data["Temperature"].replace("Hot ", "0")
data["Temperature"] = data["Temperature"].replace("Mild", "1")
data["Temperature"] = data["Temperature"].replace("Cool", "2")
data["Humidity"] = data["Humidity"].replace("High", "0")
data["Humidity"] = data["Humidity"].replace("Normal", "1")
data["Windy"] = data["Windy"].replace("Strong", "0")
data["Windy"] = data["Windy"].replace("Weak", "1")
# print(data)
temperature = int(input("How is the temperature out there? (1> Hot, 2> Mild or 3> Cold):"))
humidity = int(input("How is the humidity out there? (1> High or 2> Normal): "))
wind = int(input("What is the Force of wind? (1> Strong or 2> Weak):"))
k = 7
arr = {}
temperature -= 1
humidity -= 1
wind -= 1
length = 0
min = []
temp = data["Temperature"]
humid = data["Humidity"]
windy = data["Windy"]
weather = data["Weather"]
for i in range(len(temp)):
    ed = math.sqrt(((temperature - int(temp[i]))**2) + ((humidity - int(humid[i]))**2) + ((wind - int(windy[i]))**2))
    arr[ed] = weather[i]
sorted(arr.keys())
# print(arr)
for i, value in arr.items():
    min.append(value)
    length += 1
    if length == k:
        break
# print(arr)
c1 = min.count("Rainy")
c2 = min.count("Clear")
if c1 > c2:
    print("Weather will be rainy!!")
elif c1 < c2:
    print("Weather will be clear!!")
else:
    print("Cannot predict weather with these inputs")