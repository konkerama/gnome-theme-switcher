import configparser
import os

import logging
import sys

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s", filename="/var/log/gnome-theme-switcher.log")
logFormatter = logging.Formatter("[%(asctime)s] %(name)-12s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler(sys.stdout) #set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)

HOME = os.getenv("HOME")
BASEPATH = f"{HOME}/.config/gnome-theme-switcher"
DATAPATH = f"{BASEPATH}/data"
CONFIG_NAME = f"{BASEPATH}/config.ini"

def get_data_filename(city, country):
    return f"{BASEPATH}/data/{country.lower()}-{city.lower()}.csv"

def force_theme():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    return "force_theme" in config["Theme"]

def get_force_theme():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    return config["Theme"]["force_theme"]

def debug_force_theme():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    if "force_theme" in config["Theme"]:
        force_theme = config["Theme"]["force_theme"]
        logger.info (f"force_theme detected, setting theme to: {force_theme}")
        theme = config["Theme"][f"{force_theme}_theme"]
        return f"{force_theme},{theme}"
    else:
        print ("no force")

def get_specific_theme(theme_type):
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    return config["Theme"][f"{theme_type}_theme"]

def get_location_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    city = config["Location"]["city"]
    country = config["Location"]["country"]
    return city, country


def get_theme_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    light_theme = config["Theme"]["light_theme"]
    dark_theme = config["Theme"]["dark_theme"]
    return light_theme, dark_theme



def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_NAME)
    logger.info (config["General"]["city"])
    logger.info (config["General"]["country"])
    city = config["Location"]["city"]
    country = config["Location"]["country"]
    light_theme = config["Theme"]["light_theme"]
    dark_theme = config["Theme"]["dark_theme"]
    if "force_theme" in config["Theme"]:
        print (config["Theme"]["force_theme"])
    else:
        print ("no force")
    return config["General"]["city"], config["General"]["country"], config["General"]["light_theme"], config["General"]["dark-theme"]

