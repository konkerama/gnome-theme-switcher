#!/bin/bash

result=$(gnome-theme-switcher-selector)                                                                                                                    
echo $result
arr=(${result//,/ })

gsettings set org.gnome.desktop.interface gtk-theme "${arr[1]}" 
gsettings set org.gnome.desktop.interface color-scheme "prefer-${arr[0]}"