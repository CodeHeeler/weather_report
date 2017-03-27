import requests
from weather_classes import *


def main():
    zipcode = int(input("For which zipcode would you like a weather report? "))

    w = requests.get('http://api.wunderground.com/api/441c0489e7854381/conditions/forecast10day/astronomy/alerts/currenthurricane/q/{}.json'.format(zipcode))

    report = w.json()

    #print(report["moon_phase"]["sunset"])
    #print(report["current_observation"]["weather"])

    cc = Current_Conditions(report)
    print(cc)
    print("\n")
    tdf = Ten_Day_Forecast(report)
    print(tdf)
    print("\n")
    ss = Sunrise_Sunset(report)
    print(ss)
    print("\n")
    ca = Current_Alerts(report)
    print(ca)
    print("\n")
    ah = Active_Hurricanes(report)
    print(ah)
    print("\n")


if __name__ == "__main__":
    main()
