from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from astral import LocationInfo
import datetime
from astral.sun import sun
import csv  
import helper
import logging
import sys

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s", filename="/var/log/gnome-theme-switcher.log")

logFormatter = logging.Formatter("[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler(sys.stdout) #set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)

def get_sun_times(cityname, country, filename):
    geolocator = Nominatim(user_agent="anyName")
    coords = geolocator.geocode(f"{cityname}, {country}")
    logger.info(f"Latitude: {coords.latitude}, Longitude: {coords.longitude}")

    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=coords.longitude, lat=coords.latitude)
    logger.info(timezone)
    city = LocationInfo(cityname, country, timezone, coords.latitude, coords.longitude)

    header = ['month', 'sunrise', 'sunset']

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(1,13):
            s = sun(city.observer, date=datetime.date(2023, i, 15), tzinfo=city.timezone)
            sunrise=s["sunrise"].strftime("%H:%M:%S")
            sunset=s["sunset"].strftime("%H:%M:%S")
            logger.info(( f'Month: {i}, Sunrise: {sunrise}, Sunset: {sunset}'))
            writer.writerow([i,sunrise,sunset])

def main():
    city, country = helper.get_config()
    filename = helper.get_data_filename(city, country)
    get_sun_times(city, country, filename)

if __name__ == "__main__":
    logger.addHandler(consoleHandler)
    try:
        main()
    except Exception as e:
        logger.error("Unexpected Exception: %s" % str(e), exc_info=True)
