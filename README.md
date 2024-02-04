# Fan control for NASPi Gemini 3.5 and Raspberry Pi Debian

This script is control fan by cpu temperature on Debian.

NASPi Gemini 3.5 description: https://wiki.geekworm.com/NASPi_3.5

Debian for Raspberry Pi: https://raspi.debian.net/


## Prepare

- add **dtoverlay=pwm-2chan** to */boot/firmware/config.txt*
- add **iomem=relaxed** to */boot/firmware/cmdline.txt*


## Instalation
```shell
sudo cp -f ./fan-rpi.py /usr/local/bin/
sudo cp -f ./x-c1-fan.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable x-c1-fan
sudo systemctl start x-c1-fan
```

## Other resources
- https://wiki.geekworm.com/XScript
- https://github.com/pimlie/geekworm-x-c1
- https://github.com/geekworm-com/x-c1
- https://github.com/chattm/xscript
- https://github.com/geekworm-com/xscript
- https://github.com/geekworm-com/X885


