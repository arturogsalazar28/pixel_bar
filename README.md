# pixel_bar
Code to run a ws2813 pixel bar on raspberry pi

Uses adafruit NeoPixel library which is for 2812 leds which are similar to ws2813, just ws2813 has a backup pin, and loops through a color list on button click


Preparation & Installation
Before we install the Raspberry Pi library for the WS2812 LEDs, some preparations have to be made:

Update package sources
sudo apt-get update

Install the following packages
sudo apt-get install gcc make build-essential python-dev git scons swig

Deactivate audio output by going to the file

sudo nano /etc/modprobe.d/snd-blacklist.conf

And add the following line:
blacklist snd_bcm2835
Then the file is saved by pressing CTRL + O and CTRL + X closes the editor.

We also need to edit the configuration file:
sudo nano /boot/config.txt
Below are lines with the following content (with Ctrl + W you can search):

# Enable audio (loads snd_bcm2835)
dtparam=audio=on
This bottom line is commented out with a hashtag # at the beginning of the line: #dtparam=audio=on

We restart the system
sudo reboot
 

Now we can download the library.

git clone https://github.com/jgarff/rpi_ws281x
In this directory are on the one hand some C files included, which can be easily compiled. The example code for this is easy to understand. In order to use them in Python, we need to compile them:

cd rpi_ws281x/
sudo scons
However, in this tutorial we are mainly interested in the Python variant and therefore switch to the Python folder:

cd python
Here we carry out the installation:

sudo python setup.py build
sudo python setup.py install
This will allow us to carry out a first test in the next step.
