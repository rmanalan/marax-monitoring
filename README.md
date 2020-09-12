# Raspberry Pi Thermocouple Monitoring

![Measuring my espresso machine temp](https://preview.redd.it/1ms1uhijjnm51.jpg?width=4032&format=pjpg&auto=webp&s=0989ac597862f3f0e039913853edfe148a712159)

## What is this?

This is a simple Raspberry Pi thermocouple monitor. It uses [Adafruit's MAX31850 thermocouple amplifier](https://www.adafruit.com/product/1727). I built this so I can [monitor the temperature fluctuations on my espresso machine](https://www.reddit.com/r/espresso/comments/ir6xfn/bambino_puck_temp_monitoring/), but you can use it to measure the temperature of anything, really.

![Grafana](https://github.com/rmanalan/raspi-thermocouple-monitor/blob/master/grafana-preview.png?raw=true)

## How do I set this up?

Here are a few resources you'll need if you want to set this up yourself:

* [Raspberry Pi](https://www.raspberrypi.org/). I used a version 4 model B, but I think version 2+ should work.
* [MAX31850 thermocouple amplifier](https://www.adafruit.com/product/1727)
* [Thermocouple Type-K Glass Braid Insulated](https://www.adafruit.com/product/3245)

Here are the best instructions I found on how to wire everything together: [braveness23/Hometemp](https://github.com/braveness23/Hometemp)

![Wiring](https://raw.githubusercontent.com/braveness23/Hometemp/master/Resources/Raspberry-Pi%2BMAX31850-Thermocouple-Amplifier_bb.png)

### Running this on your Pi

First, you'll need to install Git, Docker, and Docker Compose on your Pi... google it.

Once you've installed everything, clone this repo to your Pi.

```
git clone git@github.com:rmanalan/raspi-thermocouple-monitor.git
cd raspi-thermocouple-monitor
```

Once you've done that, just simple run it:

```
sudo docker-compose up
```

Then point your browser to: http://<YOUR_PI_IP>:3000. This will open Grafana. The username and password are `admin/admin`.