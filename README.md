# readerboard
Information display using a RGB LED maxtrix and the Adafruit RGB Matrix Bonnet for Raspberry Pi. See it in action at https://www.youtube.com/watch?v=rZrlYOqqqbk

# What you will need
Raspberry Pi 4. 
2GB is fine.
8GB MicroSD card or larger

A P2 64x128 RGB LED matrix. 
These can be found from Aliexpress. If you find one that is 32x64, check the listing because sometimes they have links to the 64x128.

A 5V 10A barrel connector type DC power supply

Adafruit RGB Matrix Bonnet for Raspberry Pi
PRODUCT ID: 3211. If Adafruit is out of stock, check Digikey. 

# Hardware Install
Before we begin with the software, there is a jumper which needs to be soldered on the Adafruit RGB Matrix Bonnet.
See https://learn.adafruit.com/assets/63007 for where this jumper needs to be soldered.

Connect the ribbon cable and the postivie and negative wires to the Adafruit RGB Matrix Bonnet. Attach the ribbon cable to the input port on the P2 RGB panel and the power cable to the P2 RGB panel. Do not connect the Adafruit RGB Matrix Bonnet to the Raspberry Pi 4 at this time. 

# Software Intsall
Download the latest version of Raspian OS lite and flash it to the MicroSD card. 
Ensure that you have added the SSH file to the boot partition and optionally created your WPA_SUPPLICANT file to automatically connect to WiFi

Insert the MicroSD card into the Raspberry Pi 4 and wait for it to boot up. 

As always, run sudo apt update && sudo apt upgrade 
Here you can add an additional user if you wish and be sure to change the Pi and Root password. 

Now install the libraries to run the Adafruit RGB Matrix Bonnet
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh

During setup, there will be two prompts. One will ask what type of hat you have. Select Bonnet for that question. The second question will ask if you prefer quality or convenience. For now choose convenience but I suggest reading more about these options and see if you wish to make this change at the Adafruit site: https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices

Once the libraries have been installed, shut down the Raspberry Pi 4 and install the Adafruit RGB Matrix Bonnet. Now is a good time to ensure that the cables are connected correctly especially the polarity of the power. Plug in the 5V 10A power supply into the Adafruit RGB Matrix Bonnet and it will begin to boot up. 

Don't be alarmed if there are some random lights flashing on the RGB board. 

# Time to test

Log back into the Raspberry Pi 4 and locate the directly rpi-rgb-led-matrix/bindings/python/samples
Run sudo python pulsing-colors.py and there should be pulshing colors on the board
Other sample programs will not line up correctly because it is not aware of the geometry which is fine. 

# Clone the Readerboard program

Now clone this program and open up settings.py
Visit https://alerts.weather.gov/ and scroll down to your state to locate your Weather Alert Zone
Click the Zones link and find the zone which is closest to your area and enter that code into weatherAlertCode="NNN000"
Go back one page and now click Counties and find the code for your county. Enter that code into weatherForecastCode="NNN000"

News feeds are RSS based. Currently they are set to read from Reddit news, news of the weird, and not the onion. They can be changed
to whatever news feeds you like. If there are any topics you do not wish to see, simply enter keywords into the excludeList. 

# Before running

Most Python libraries should already be installed; however, you may need to install the following:

pip install feedparser
pip install sockets
pip install supyr_struct
pip install Pillow

You will also need to download and install the following to fonts into your fonts folder:
VCR_OSD_MONO_1.001.ttf
arial.ttf

# Running

The program must be run as sudo
sudo python3 readerboard.py

# Final notes

I am not a professional Python programmer by any means and I know this code is a mess. It has worked for me for quite a while. There are some fixes I need to do such as exception handling when a reporting weather station isn't reporting any weather. I also want to change the way the weather alerts are tracked. 

That being said, this should never be your primary means for weather information and should be considered for entertainment purposes only. 



