<h1>MakeLatex</h1>
<h3>Usage: "./makelatex (hw number)"</h3>
About: Scrapes URL from Aviv's website, parses HTML and generates a decent looking latex document for the HW.<br>
Author: Benjamin Birney

<h3>Installing Python / Dependent Libraries:</h3>
- Install / Update Python<br>
  * Run "python --version" (You should be running something around 3.6)<br>
  * If you don't have python, then run "sudo apt-get update ; sudo apt-get install python3.6"<br>
- Installing necessary libraries / other stuff<br>
  * Check you pip version (if you have one) by running "pip --version"<br>
  * Install pip (if you don't have it) by running "sudo apt-get install python-pip python-dev build-essential"<br>
  * Next run "sudo easy_install pip" then "sudo pip install --upgrade virtualenv"<br>
  * To install BS4 (a dependency of the script) run "pip install beautifulsoup4"
<h3>Disclaimers:</h3>
- Download the script & place the actual directory wherever you want to run it (i.e. your bin)<br>
- Make sure to run "sudo chmod +x makelatex" in your favorite directory<br>
- If you have any trouble with stuff, feel free to ask me for help (or to google your problem)<br>
- Also feel free to dig around in the script. The code is commented, so it shouldn't be too 
  hard to figure out what I'm doing<br>
