#!/bin/bash

sudo -u $USER DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=$DBUS_SESSION_BUS_ADDRESS change-theme >> /var/log/gnome-theme-switcher.log