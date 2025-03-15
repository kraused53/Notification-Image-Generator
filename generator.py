import requests
from weather_codes import get_weather_icon_from_code
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime

# Icon directory
icon_dir = "./icons/"

# Image Settings
IM_W = 400
IM_H = 300

ICON_W = 175
ICON_H = 175
ICON_X = int( int( IM_W / 2 ) - int( ICON_W /2 ) )
ICON_Y = int( int( IM_H / 2 ) - int( ICON_H /2 ) )

TEMP_W = IM_W - ICON_W
TEMP_H = ICON_H
TEMP_X = ICON_X + ICON_W
TEMP_Y = 0

INFO_W = IM_W
INFO_H = IM_H - ICON_H
INFO_X = 0
INFO_Y = ICON_Y + ICON_H

# API request URL
API_URL = (
    # Base URL
    "https://api.open-meteo.com/v1/forecast?"
    # Location
    "latitude=38.2542&longitude=-85.7594"
    # Request Current Weather
    "&current="
    "temperature_2m,"
    "precipitation,"
    "weather_code,"
    "wind_speed_10m,"
    "rain,"
    "cloud_cover,"
    "wind_direction_10m,"
    "is_day,"
    "snowfall,"
    "surface_pressure,"
    "wind_gusts_10m,"
    "showers,"
    "pressure_msl,"
    "relative_humidity_2m,"
    "apparent_temperature"
    # Request Daily
    "&daily="
    "precipitation_probability_max"
    # Timezone
    "&timezone=America%2FNew_York"
    # Units
    "&wind_speed_unit=mph"
    "&temperature_unit=fahrenheit"
    "&precipitation_unit=inch"
    "&timeformat=unixtime"
)


def convert_icon_background(icon):
    # Break image into individual pixels
    pix = icon.load()

    # If given object is a .PNG file
    if icon.mode == 'RGBA':
        # Check every pixel in the image
        for y in range(icon.size[1]):
            for x in range(icon.size[0]):
                # If pixel has a transparency value that is anything other that solid
                if pix[x, y][3] < 255:
                    # Convert the pixel to a solid white one
                    pix[x, y] = (255, 255, 255, 255)
    # Return the adjusted image pixels
    return pix

if __name__ == "__main__":
    print(API_URL)
    '''
        Get weather forecast and convert to json
    '''
    response = requests.get( API_URL )
    data = response.json()

    '''
        Create blank image
    '''
    img = Image.new('RGBA', (IM_W, IM_H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    '''
        Get date-time
    '''
    unix_time = datetime.now()

    font = ImageFont.truetype("arial.ttf", 20)

    cur_date = unix_time.strftime("%b. %d, %Y")
    cur_time = unix_time.strftime("%I:%M %p")

    tw = font.getlength(cur_date)
    tx = (int(IM_W / 2) - int(tw / 2))
    ty = 35
    draw.text((tx, ty), cur_date, (0, 0, 0), font)

    tw = font.getlength(cur_time)
    tx = (int(IM_W / 2) - int(tw / 2))
    ty = 10
    draw.text((tx, ty), cur_time, (0, 0, 0), font)

    if "current" in data:
        '''
            Get Weather Icon and add to image
        '''
        icon_path = None
        if "weather_code" in data["current"]:
            if "is_day" in data["current"]:
                if data["current"]["is_day"] == int(1):
                    icon_path = icon_dir + get_weather_icon_from_code(int(data["current"]["weather_code"]), True)
                else:
                    icon_path = icon_dir + get_weather_icon_from_code(int(data["current"]["weather_code"]), False)
        if icon_path is not None:
            icon = Image.open(icon_path)
            pixels = convert_icon_background(icon)
            img.paste(icon, (ICON_X, ICON_Y))

        '''
            Get Temperature
        '''
        if "temperature_2m" in data["current"]:
            cur_temp = str(data["current"]["temperature_2m"]) + "°F"

            font = ImageFont.truetype("arial.ttf", 56)
            l, t, r, b = font.getbbox( cur_temp )
            tw = font.getlength(cur_temp)
            tx = ( int( IM_W / 4 ) -  int( tw / 2 ) )
            ty = ( IM_H - 60 )

            draw.text((tx, ty), cur_temp, (0, 0, 0), font)

        '''
            Get Humidity
        '''
        if "relative_humidity_2m" in data["current"]:
            cur_hum = str(data["current"]["relative_humidity_2m"]) + " %"

            font = ImageFont.truetype("arial.ttf", 56)
            l, t, r, b = font.getbbox( cur_hum )
            tw = font.getlength(cur_hum)
            tx = ( int( 3 * IM_W / 4 ) -  int( tw / 2 ) )
            ty = ( IM_H - 60 )

            draw.text((tx, ty), cur_hum, (0, 0, 0), font)

        '''
            Shabbat / Havdalah
            Shabbat is from Friday Sundown to Saturday Sundown
            Havdalah is from Saturday sundown to sunday sunrise
        '''
        # TODO


    draw.line( [ (0, ICON_Y), (IM_W, ICON_Y) ], ( 0, 0, 0 ) )

    img.show()
