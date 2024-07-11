# Installation 

Test Equipment: HMP4040 by Rohde & Schwarz
-currently tested on windows 10
-does not work on mac m1 arm64 (only device recognition done but doesn't connect)
-haven't tested on linux

This project requires a couple of libraries
I installed a ton of things to get this thing working, from keysight library suite to HMExplorer to pycharm plugin for Rohde and to 3rd party libraries for accessing through python but none of them worked. the instrument would just not be returned when queried for presence. 

At the end the following setup worked:

- Driver for the instrument. download the VCP (virtual com port) driver to access the device via usb. the devices are usually setup with FTDI as can be seen from the drivers files. so that gave me a hint to not use the usual libraries like VISA or pyvisa to access it. i simply did it with pyserial to access com port
- check you device manager to see if a new com port is added 
- download the driver and udpate the driver with the VCP driver
- run "pip install pyserial" in terminal(python library for accessing comports) 
- run aliveTest.py to check if the instrument replies. and voila. (you'll need to change comport, baudrate as per instruments programming manual)
- the commands starting with a '*' are universal and will be applicable for all instruments. 
- depending on your instrument it might require you to append all your commands with a '\n' mine does so keep that in mind. 

# My setup (Optional)
Since my main system is a mac m1 (arm64) i wanted to connect all my instruments to a remote system which i can access. only need the windows for the drivers (yes i did try VM and parallels.. didn't work, ran out of patience). 

for accessing the target system remotely 
- install openssh server (in target)
- need to have ssh client on client (my mac doesn't need it. comes pre installed)
- once connected run the python program which continously poles for required data and the output is piped to your mac. 

on target, execute:
```bash
chmod +x hmp4040_remote.sh
```
I'm using ENV file to store remote host etc for ease of use you need to make your own ENV file and provide that. if not then type that directly into .sh file. 

# General case
Say you have 4 instruments. all you need to do is create 4 instances of pyserial query as you see fit, save output to a csv in a nice formatted way. and graph it possibly using matplotlib and access those graph.. can be done in a live environment. 
