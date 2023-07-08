# gnome-theme-switcher

Small utility to schedule theme change between light and dark theme. It checks the local time and based on if the sun is out or down it will change the theme to the preselected light or dark respectively.

## Setup 
### Install from source

#### Prerequisites

- Gnome Environment (has been tested on ubuntu 22)
- Python installed and running (tested on python3.11)
- Install [pyinstaller](https://pyinstaller.org/en/stable/installation.html)

#### Config
Open `config.ini` and configure it with your city/country details and your preferred light and dark theme.
If you want to test the theme switch without waiting for the next sunrise/sunset you can set the `force_theme` to light/dark based on your preference.

#### Install 
clone repository locally and run:

``` bash
make 
```

#### Cleanup 
To cleanup do:

``` bash
make cleanup
```

### Prebuilt Binaries
Todo

## Logs
The utitly places its logs in the `/var/log/gnome-theme-switcher.log` file