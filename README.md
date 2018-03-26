<h1>MakeLatex</h1>
<h3>Usage: "./makelatex (hw number)"</h3>
About: Scrapes URL from Aviv's website, parses HTML and generates a decent looking latex document for the HW.<br>
Author: Benjamin Birney

<h3>Installing Python / Dependent Libraries:</h3>
- Install / Update Python
  - Run "python --version" (You should be running something around 3.6)
  - If you don't have python, then run "sudo apt-get update ; sudo apt-get install python3.6"
- Installing necessary libraries / other stuff
  - Check you pip version (if you have one) by running "pip --version"
  - Install pip (if you don't have it) by running "sudo apt-get install python-pip python-dev build-essential"
  - Next run "sudo easy_install pip" then "sudo pip install --upgrade virtualenv"
  - To install BS4 (a dependency of the script) run "pip install beautifulsoup4"
<h3>Disclaimers:</h3>
- Download the script & place the actual directory wherever you want to run it (i.e. your bin)
- Make sure to run "sudo chmod +x makelatex" in your favorite directory
- If you have any trouble with stuff, feel free to ask me for help (or to google your problem)
- Also feel free to dig around in the script. The code is commented, so it shouldn't be too hard to figure out what I'm doing
