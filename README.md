# Fan control and work with power button for NASPi Gemini 3.5 and Raspberry Pi Debian

This script is control fan by cpu temperature and work with hardware button on Debian.

NASPi Gemini 3.5 description: https://wiki.geekworm.com/NASPi_3.5

Debian for Raspberry Pi: https://raspi.debian.net/


## Prepare

- add **dtoverlay=pwm-2chan** to */boot/firmware/config.txt*\
(for persistent after reboot add to /etc/default/raspi-firmware-custom)
```shell
root@rpi:~# cat /etc/default/raspi-firmware-custom
dtoverlay=pwm-2chan
```
- add **iomem=relaxed** to */boot/firmware/cmdline.txt*


## Instalation
```shell
sudo cp -f ./fan-rpi.py /usr/local/bin/
sudo cp -f ./pwr-rpi.py /usr/local/bin/
sudo cp -f ./x-c1-fan.service /lib/systemd/system/
sudo cp -f ./x-c1-pwr.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable x-c1-fan
sudo systemctl start x-c1-fan
sudo systemctl enable x-c1-pwr
sudo systemctl start x-c1-pwr
```

## Other resources
- https://wiki.geekworm.com/XScript
- https://wiki.geekworm.com/X-C1_Software
- https://github.com/pimlie/geekworm-x-c1
- https://github.com/geekworm-com/x-c1
- https://github.com/chattm/xscript
- https://github.com/geekworm-com/xscript
- https://github.com/geekworm-com/X885


