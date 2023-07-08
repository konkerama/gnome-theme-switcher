#!/bin/bash

sudo -u $USER DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=$DBUS_SESSION_BUS_ADDRESS gnome-theme-switcher >> /var/log/gnome-theme-switcher.log