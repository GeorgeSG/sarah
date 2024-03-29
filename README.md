![S.A.R.A.H.](assets/eureka.sarah.jpg?raw=true)

# S.A.R.A.H

[![Commit Activity](https://img.shields.io/github/commit-activity/m/GeorgeSG/sarah)](https://github.com/GeorgeSG/sarah)
[![Build Status](https://travis-ci.com/GeorgeSG/sarah.svg?token=XdvzWyHdX7CysRsYcThK&branch=master)](https://travis-ci.com/GeorgeSG/sarah)

### Self Actuated Residential Automated Habitat

This is my [Home Assistant](https://home-assistant.io/) configuration :)

[Ping me](#meta) with any questions.

## Configuration

I'm using [Home Assistant Packages](https://www.home-assistant.io/docs/configuration/packages/) to
keep everything organized and grouped by different functionalities.

- `devices` - configuration and behavior for specific devices
- `modules` - major functions / behaviors are split into modules
- `modes` - entering and exiting house modes
- `routines` - definitions of automated routines - e.g. Coming Home or Waking Up
- `sensors` - describing sensors the house can use

The `speech` module uses [partial templates](https://github.com/GeorgeSG/sarah/tree/master/config/templates/partials) to generate more complex messages.

## Hardware

**Servers:**

- [Intel NUC6i7KYK](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc6i7kyk.html) - Ubuntu running Home Assistant and Plex Media Server
- [Synology DS1821+](https://www.synology.com/en-global/products/DS1821+) - Synology NAS Server
- [Synology DS415play](https://www.synology.com/) - Synology NAS Server (backup)

**Controllers:**

- [ConBee II](https://www.phoscon.de/en/conbee2) - Zigbee controller
- [aeotec Z-Stick gen 5](https://aeotec.com/z-wave-usb-stick/index.html) - Zwave controller

**Sensors & Switches:**

- [Aqara Temperature and Humidity Sensor](https://www.aqara.com/us/temperature_humidity_sensor.html) (Zigbee)
- [Aqara Door and Window Sensor](https://www.aqara.com/us/door_and_window_sensor.html) (Zigbee)
- [Aqara Wireless Mini Switch](https://www.aqara.com/en/smart_wireless_mini_switch.html) (Zigbee)
- [Aqara Motion Sensor](https://www.aqara.com/eu/motion_sensor.html) (Zigbee)
- [Aeotec MultiSensor 6](https://aeotec.com/z-wave-sensor/index.html) (Zwave)
- [Aeotec Trisensor](https://aeotec.com/z-wave-motion-sensor/index.html) (Zwave)
- [Aeotec WallMote](https://aeotec.com/z-wave-wireless-switch/index.html) (Zwave - 4-button switch)
- [Aqara Opple Wireless](https://zigbee.blakadder.com/Xiaomi_WXCJKG13LM.html) (Zigbee - 6-button switch)

**Lights:**

- [Philips Hue White & Color Ambiance E14](https://www.philips-hue.com/en-us/p/hue-white-and-color-ambiance-single-bulb-e12/046677556969)
- [Philips Hue White Ambiance E14](https://www.philips-hue.com/en-us/p/hue-white-ambiance-single-bulb-e12/046677556976)
- [Philips Hue White E14](https://www.philips-hue.com/en-us/p/hue-white-2-pack-e12/046677548285)
- A bunch of random Tuya E14 lights (wifi - some flashed with Tasmota, some runing on Tuya Cloud)
- [Yeelight S1 Lights](https://www.yeelight.com/en_US/product/lemon2-color) (wifi)

A note on lights - I tried a lot of wifi lights, running on Tuya Cloud, running with Tasmota; also
tried some Zigbee ones as well. They all broke or had issues - blinking, noise, etc. The Hues are
expensive, but I would have saved money if I went with them from the start.

**Media:**

- [LG C8 TV](https://www.lg.com/uk/tvs/lg-OLED55C8PLA) with [NVidia Shield TV Pro](https://www.nvidia.com/en-us/shield/shield-tv-pro/)
- [Sonos One](https://www.sonos.com/en-us/shop/one.html)
- [Sonos Beam](https://www.sonos.com/en-us/shop/beam.html)

**Misc:**
- [Philips AC2729 Air Purifier and Humidifier](https://www.p4c.philips.com/cgi-bin/cpindex.pl?scy=EE&slg=EN&ctn=AC2729/10) (wifi)
- [Hama Wifi Socket](https://de.hama.com/00176565/hama-wifi-socket-with-integrated-current-measuring-device-3680-w-16-a) (wifi - Tasmota / MQTT)
- [FrankEver IR Remote Controller](https://www.amazon.com/Controller-Universal-Infrared-Repeater-Compatible/dp/B07ZP5NQWF) (wifi - Tasmota / MQTT)
- [Soma Smart Shades](https://www.somasmarthome.com/) (wifi)
- Amcrest Security Camera
- Tapo Security Camera

## Screenshots (v3)

![Living Room](assets/screenshot-v3-living-room.png?raw=true)
![Living Room 2](assets/screenshot-v3-living-room-2.png?raw=true)
![Bedroom](assets/screenshot-v3-bedroom.png?raw=true)
![Kitchen](assets/screenshot-v3-kitchen.png?raw=true)

## Screenshots (Legacy UI - v2)

### Home

![Home screen](assets/screenshot-home.png?raw=true)

### Network

![Network screen](assets/screenshot-network.png?raw=true)

### Floorplan

![Floorplan](assets/screenshot-floorplan.png?raw=true)

## Helpers

There are some useful scripts in `./bin`.

In order to use them, copy `./bin/.env.example` to `./bin/.env` and set the correct values.
You must be able to ssh to the host with a ssh key.

- `./bin/ui` - re-uploads only UI configuration files
- `./bin/upload` - re-uploads all configuration files
- `./bin/restart` - restarts Home Assistant via docker-compose
- `./bin/update` - `upload` and then `restart`
- `./bin/logs` - tails the logs of Home Assisstant via docker-compose

## Inspiration

1. [CCOSTAN/Home-AssistantConfig](https://github.com/CCOSTAN/Home-AssistantConfig)
1. [lukevink/hass-config-lajv](https://github.com/lukevink/hass-config-lajv)
1. [matt8707/hass-config](https://github.com/matt8707/hass-config)
1. [stanvx/Home-Assistant-Configuration](https://github.com/stanvx/Home-Assistant-Configuration)
1. [Apocrathia/home-assistant-config](https://github.com/Apocrathia/home-assistant-config)
1. [geekofweek/homeassistant](https://github.com/geekofweek/homeassistant)

## Meta

[1.1]: http://i.imgur.com/wWzX9uB.png
[2.1]: http://i.imgur.com/9I6NRUm.png

**Georgi Gardev**

- [gar.dev](https://gar.dev)
- [![GitHub][2.1]](https://github.com/GeorgeSG/) [GeorgeSG](https://github.com/GeorgeSG/)
- [![Twitter][1.1]](https://twitter.com/georgesg92) [@georgesg92](https://twitter.com/georgesg92)
