import time
import pandas
import os

while True:
    if os.path.exists("weather.csv"):
        data = pandas.read_csv("weather.csv")
        print(data.mean()["st1"])

        time.sleep(2)
