Author: Benjamin Birney

Usage: "./makelatex <hw number>"

About: Scrapes URL from Aviv's website, parses HTML and generates a decent looking latex document for the HW.

Installing Python / Dependent Libraries:
- Install / Update Python
  - Run "python --version" (You should be running something around 3.6)
  - If you don't have python, then run "sudo apt-get update ; sudo apt-get install python3.6"
- Installing necessary libraries / other stuff
  - Check you pip version (if you have one) by running "pip --version"
  - Install pip (if you don't have it) by running "sudo apt-get install python-pip python-dev build-essential"
  - Next run "sudo easy_install pip" then "sudo pip install --upgrade virtualenv"
  

Disclaimers:
1) RUN "sudo chmod +x makelatex" AND PUT FILE IN "/bin/" OR ".local/bin" OR "/usr/bin/"
2) MAKE SURE YOU UPDATE YOUR PYTHON LIBRARIES OR IT WON'T WORK
3) IF YOU DON'T HAVE A PACKAGE PLS DOWNLOAD
