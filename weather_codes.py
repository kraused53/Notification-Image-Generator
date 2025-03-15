import typing

def get_weather_from_code( code: int ) -> str:
    ret = ""

    if code == 0:
        ret = "Clear Sky"
    elif code == 1:
        ret = "Slightly Cloudy"
    elif code == 2:
        ret = "Moderately Cloudy"
    elif code == 3:
        ret = "Overcast"
    elif code == 45:
        ret = "Fog"
    elif code == 48:
        ret = "Rime Fog"
    elif code == 51:
        ret = "Light  Drizzle"
    elif code == 53:
        ret = "Moderate Drizzle"
    elif code == 55:
        ret = "Dense Drizzle"
    elif code == 56:
        ret = "Light Freezing Drizzle"
    elif code == 57:
        ret = "Dense Freezing Drizzle"
    elif code == 61:
        ret = "Light Rain"
    elif code == 63:
        ret = "Moderate Rain"
    elif code == 65:
        ret = "Heavy Rain"
    elif code == 66:
        ret = "Light Freezing Rain"
    elif code == 67:
        ret = "Heavy Freezing Rain"
    elif code == 71:
        ret = "Light Snow Fall"
    elif code == 73:
        ret = "Moderate Snow Fall"
    elif code == 75:
        ret = "Heavy Snow Fall"
    elif code == 77:
        ret = "Snow Grains"
    elif code == 80:
        ret = "Slight Rain Shower"
    elif code == 81:
        ret = "Moderate Rain Shower"
    elif code == 82:
        ret = "Heavy Rain Shower"
    elif code == 85:
        ret = "Slight Snow Shower"
    elif code == 86:
        ret = "Heavy Snow Shower"
    else:
        ret = "Unknown Weather Code"

    return ret

def get_weather_icon_from_code( code: int, is_day: bool ) -> str:
    ret = ""

    if is_day:
        if code == 0:
            ret = "sun.png"
        elif code == 1:
            ret = "day-cloudy.png"
        elif code == 2:
            ret = "day-very-cloudy.png"
        elif code == 3:
            ret = "overcast.png"
        elif code == 45:
            ret = "day-fog.png"
        elif code == 48:
            ret = "day-fog.png"
        elif code == 51:
            ret = "rain.png"
        elif code == 53:
            ret = "rain.png"
        elif code == 55:
            ret = "rain.png"
        elif code == 56:
            ret = "rain.png"
        elif code == 57:
            ret = "rain.png"
        elif code == 61:
            ret = "rain.png"
        elif code == 63:
            ret = "rain.png"
        elif code == 65:
            ret = "rain.png"
        elif code == 66:
            ret = "rain.png"
        elif code == 67:
            ret = "rain.png"
        elif code == 71:
            ret = "snow.png"
        elif code == 73:
            ret = "snow.png"
        elif code == 75:
            ret = "snow.png"
        elif code == 77:
            ret = "snow.png"
        elif code == 80:
            ret = "rain.png"
        elif code == 81:
            ret = "rain.png"
        elif code == 82:
            ret = "rain.png"
        elif code == 85:
            ret = "snow.png"
        elif code == 86:
            ret = "snow.png"
        elif code == 95:
            ret = "day-storm.png"
        else:
            ret = "sun.png"
    else:
        if code == 0:
            ret = "moon.png"
        elif code == 1:
            ret = "night-cloudy.png"
        elif code == 2:
            ret = "night-very-cloudy.png"
        elif code == 3:
            ret = "overcast.png"
        elif code == 45:
            ret = "night-fog.png"
        elif code == 48:
            ret = "night-fog.png"
        elif code == 51:
            ret = "rain.png"
        elif code == 53:
            ret = "rain.png"
        elif code == 55:
            ret = "rain.png"
        elif code == 56:
            ret = "rain.png"
        elif code == 57:
            ret = "rain.png"
        elif code == 61:
            ret = "rain.png"
        elif code == 63:
            ret = "rain.png"
        elif code == 65:
            ret = "rain.png"
        elif code == 66:
            ret = "rain.png"
        elif code == 67:
            ret = "rain.png"
        elif code == 71:
            ret = "snow.png"
        elif code == 73:
            ret = "snow.png"
        elif code == 75:
            ret = "snow.png"
        elif code == 77:
            ret = "snow.png"
        elif code == 80:
            ret = "rain.png"
        elif code == 81:
            ret = "rain.png"
        elif code == 82:
            ret = "rain.png"
        elif code == 85:
            ret = "snow.png"
        elif code == 86:
            ret = "snow.png"
        elif code == 95:
            ret = "storm.png"
        else:
            ret = "night-moon.png"


    return ret