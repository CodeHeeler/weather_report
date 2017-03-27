class Current_Conditions:
    def __init__(self, report):
        self.weather = report["current_observation"]["weather"]
        self.temp_string = report["current_observation"]["temp_f"]
        self.wind_string = report["current_observation"]["wind_string"]

    def __repr__(self):
        return "Currently: {}\nTemperature: {}\nWind: {}".format(self.weather, self.temp_string, self.wind_string)


class Ten_Day_Forecast:
    def __init__(self, report):
        self.ten_day = report["forecast"]["txt_forecast"]["forecastday"]

    def basic_ten_day(self):
        basic = []
        for day in self.ten_day:
            basic.append((day["title"], day["fcttext"]))
        return basic

    def __repr__(self):
        basic = self.basic_ten_day()
        text = ""
        for tup in basic:
            text += "{}:\n{}\n\n".format(tup[0], tup[1])
        return "Ten Day Forecast:\n\n{}".format(text)


class Sunrise_Sunset:
    def __init__(self, report):
        self.sunrise = report["sun_phase"]["sunrise"]
        self.sunset = report["sun_phase"]["sunset"]

    def __repr__(self):
        return "Sunrise: {}:{}\nSunset: {}:{}".format(self.sunrise["hour"], self.sunrise["minute"], self.sunset["hour"], self.sunset["minute"])


class Current_Alerts:
    def __init__(self, report):
        self.alerts = report["alerts"]

    def __repr__(self):
        if self.alerts:
            return self.alerts
        else:
            return "There are no current alerts for this area."


class Active_Hurricanes:
    def __init__(self, report):
        self.hurricanes = report["currenthurricane"]

    def __repr__(self):
        if self.hurricanes:
            nice_names = []
            for storm in self.hurricanes:
                nice_names.append(storm["stormInfo"]["stormName_Nice"])
            return "Current Hurricanes: {}".format(nice_names)
        else:
            return "There are no hurricanes currently."
