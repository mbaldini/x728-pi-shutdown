# x728-pi-shutdown
Clean shutdown script for an x728 UPS board on a raspberry pi.

Used with the [Geekworm x728 UPS hat for raspberry pi](https://geekworm.com/products/raspberry-pi-x728-max-5-1v-8a-18650-ups-power-management-board).

This simple pythons script will trigger the onboard buzzer to beep once (pin 20), followed by sending a signal to pin 6.

## Requirements
* [Geekworm x728 UPS hat for raspberry pi](https://geekworm.com/products/raspberry-pi-x728-max-5-1v-8a-18650-ups-power-management-board)
* Raspberry Pi (tested on both rpi 2B+ and rpi 3)
* I2C enabled on raspberry pi


## Enabling I2C on Raspberry Pi

Open the terminal and enter:

`sudo raspi-config`

Select number 5 'interface options'

![Interface Options](https://github.com/mbaldini/x728-pi-shutdown/blob/main/images/Rpi-config-1.jpg?raw=true)

Select 'P5 I2C - Enable/Disable automatic loading of I2C kernel module'

![Enable/Disable I2C](https://github.com/mbaldini/x728-pi-shutdown/blob/main/images/Rpi-config-5.jpg?raw=true)

You should see the following:

![I2C Enabled](https://github.com/mbaldini/x728-pi-shutdown/blob/main/images/Rpi-config-6.jpg?raw=true)

Select 'ok' followed by 'finish' to return to the terminal console.


## Required software installation for x728 hardware

1. login via teminal window, then update & upgrade

```
sudo apt-get update
sudp apt-get upgrade
sudo reboot
```

2. Install necessary software (python and i2c tool library)

```
sudo apt-get -y install python-smbus i2c-tools
```

3. Download x728 setup scripts:

```
cd ~
git clone https://github.com/geekworm-com/x728
cd x728
chmod +x *.sh
```

4. Install script&reboot:

Firstly please select your x728 version

```
sudo bash x728-v2.1.sh
```

#New add buzzer support

or

```
sudo bash x728-v2.0.sh
```

or

```
sudo bash x728-v1.0.sh
```

then

```
sudo reboot
```

You can get the following python file in /home/pi/ folder:

```
x728bat.py # Reading battery voltage
x728pld.py # Script to detect when power loss occurs, waits for 10 seconds, then sends the soft shutdown signal to the x728 and shuts down the pi.
```

5. Set and Read the RTC time

```
#If you need to set the system time for any reason you can use the following command :  
date -s "5 MAR 2019 13:00:00"
#Write the system date and time to the RTC module after your correct the system date and time :  
sudo hwclock -w
#Read the date and time back from the RTC module:  
sudo hwclock -r
```

6. How to reading battery voltage and percentage, this is the sample code, you can modify it by your request.

```
sudo python /home/pi/x728bat.py
```

