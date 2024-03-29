all: install gnome-theme-switcher deploy setup_logging cron

install:
	pip install -r requirements.txt

gnome-theme-switcher: 
	pyinstaller --onefile --clean src/gnome-theme-switcher-selector.py
	cp src/gnome-theme-switcher.sh dist/gnome-theme-switcher

deploy: gnome-theme-switcher
	sudo cp dist/gnome-theme-switcher /usr/local/bin
	sudo cp dist/gnome-theme-switcher-selector /usr/local/bin

setup_logging:
	sudo touch /var/log/gnome-theme-switcher.log
	sudo chown ${USERNAME}:${USERNAME} /var/log/gnome-theme-switcher.log
	chmod 666 /var/log/gnome-theme-switcher.log

cron:
	envsubst < src/cron-gnome-theme-switcher.sh > dist/cron-gnome-theme-switcher
	sudo cp dist/cron-gnome-theme-switcher /etc/cron.hourly/
	sudo chmod 775 /etc/cron.hourly/cron-gnome-theme-switcher

copy_config:
	mkdir -p ${HOME}/.config/gnome-theme-switcher/data
	cp config.ini ${HOME}/.config/gnome-theme-switcher

cleanup:
	sudo rm /usr/local/bin/gnome-theme-switcher
	sudo rm /etc/cron.hourly/cron-gnome-theme-switcher
	sudo rm /var/log/gnome-theme-switcher -r
	rm ~/.config/gnome-theme-switcher -r
