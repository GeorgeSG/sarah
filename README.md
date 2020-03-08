![S.A.R.A.H.](assets/eureka.sarah.jpg?raw=true)

# S.A.R.A.H

![](https://img.shields.io/github/commit-activity/m/GeorgeSG/sarah)

### Self Actuated Residential Automated Habitat

This is my [Home Assistant](https://home-assistant.io/) configuration :)

[Ping me](#meta) with any questions.

## Hardware

**Servers:**

- [Intel NUC6i7KYK](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc6i7kyk.html) - Ubuntu running Home Assistant and Plex Media Server
- [Synology DS415play](https://www.synology.com/) - Synology NAS Server

**Controllers:**

- [ConBee II](https://www.phoscon.de/en/conbee2) - ZigBee controller

**Sensors:**

- [Aqara Temperature and Humidity Sensor](https://www.aqara.com/us/temperature_humidity_sensor.html)
- [Aqara Door and Window Sensor](https://www.aqara.com/us/door_and_window_sensor.html)

**Lights:**

- A bunch of random Tuya E14 lights
- [Yeelight S1 Lights](https://www.yeelight.com/en_US/product/lemon2-color)

**Media:**

- [LG C8 TV](https://www.lg.com/uk/tvs/lg-OLED55C8PLA) with [NVidia Shield TV Pro ](https://www.nvidia.com/en-us/shield/shield-tv-pro/)
- [Sonos One](https://www.sonos.com/en-us/shop/one.html)

**Misc:**

- [Aqara Magic Cube](https://www.gearbest.com/access-control/pp_1845856.html)
- [Philips AC2729 Air Purifier and Humidifier](https://www.p4c.philips.com/cgi-bin/cpindex.pl?scy=EE&slg=EN&ctn=AC2729/10)
- Amcrest Security Camera

## Configuration

I'm using [Home Assistant Packages](https://www.home-assistant.io/docs/configuration/packages/) to
keep everything organized and grouped by different functionalities.

- `devices` - configuration and behavior for specific devices
- `modules` - major functions / behaviors are split into modules
- `modes` - entering and exiting house modes
- `routines` - definitions of automated routines - e.g. Coming Home or Waking Up
- `sensors` - describing sensors the house can use

The `speech` module uses [partial templates](https://github.com/GeorgeSG/sarah/tree/master/templates/partials) to generate more complex messages.

## Screenshots

### Home

![Home Screen](assets/screenshot-home.png?raw=true)

## Inspiration

1. [Bear Stone Smart Home Documentation](https://github.com/CCOSTAN/Home-AssistantConfig)
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
