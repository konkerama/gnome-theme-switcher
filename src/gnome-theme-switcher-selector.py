import datetime
import os
import csv
import setup
import helper
import logging
import sys

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s", filename="/var/log/gnome-theme-switcher.log")

logFormatter = logging.Formatter("[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler(sys.stdout) #set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)
# logger.addHandler(consoleHandler)

def check_file(city, country, filename):
    if not os.path.isfile(filename):
        logger.info("file does not exist, gathering data")
        setup.get_sun_times(city, country, filename)
    else:
        logger.info ("retrieving data from existing csv")

def get_current_month():
    now = datetime.datetime.now()
    current_month = str(now.month)
    logger.info(f"Current Month: {current_month}")
    return current_month

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    logger.info(f"Current Time: {current_time}")
    return current_time

def get_current_months_sun_times(current_month, filename):
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0]==current_month:
                logger.info(row)
                sunrise=row[1]
                sunset=row[2]
                return sunrise,sunset

def main():
    city, country = helper.get_location_config()
    light_theme, dark_theme = helper.get_theme_config()
    if helper.force_theme():
        force_theme=helper.get_force_theme()
        logger.info (f"force_theme detected, setting theme to: {force_theme}")
        theme=helper.get_specific_theme(force_theme)
        print (f"{force_theme},{theme}")
        return
    filename = helper.get_data_filename(city, country)
    check_file(city, country, filename)
    current_month = get_current_month()
    current_time = get_current_time()
    sunrise, sunset = get_current_months_sun_times(current_month, filename)
    if (current_time > sunrise) and (current_time < sunset):
        logger.info ("Sun is out, switching to light theme")
        print(f"light,{light_theme}")
    else: 
        logger.info ("Sun is down, switching to dark theme")
        print(f"dark,{dark_theme}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("Unexpected Exception: %s" % str(e), exc_info=True)
