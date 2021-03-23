import os, socket, webbrowser #requests
from requests import get
from pyconsole import *

titleDir = os.path.join(projectDir, "titles")

# Functions
# Main startup screen
def MainDashboard():
    ClearScreen()
    titles = ListFiles(titleDir, "title-project-roanoke")
    titleColors = [Color.BrightCyan, Color.BrightYellow, Color.BrightGreen, Color.BrightYellow, Color.BrightGreen]
    titleNumber = 0
    for title in titles:
        content = open(title)
        PrintMessage(content.read(), "none", titleColors[titleNumber])
        titleNumber += 1

    UserInput()

# Searches for files in a directory matching the filter
def ListFiles(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().startswith(filetype.lower()):
            paths.append(os.path.join(root, file))

   return paths

# Checks that the users input is a valid number between 1-18
def UserInput():
    userInput = input("Please select a program 1-18: ")
    try:
        value = int(userInput)
        if value > 18:
            PrintMessage("Number is greater than 18.", "Error")
            UserInput()

        elif value < 0:
            PrintMessage("Why would you think to use negative numbers? How would that even work?", "Error")
            UserInput()

        elif value == 0:
            PrintMessage("Please enter a number greater than 0.", "Error")
            UserInput()

        # Start of selection elif statments
        # Selection: 1 - Opens web rickroll - Temporary
        elif value == 1:
            PrintMessage("Booting selected program. This may take a second...")
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get("chrome").open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        # Selection: 2 - Opens Fern Wifi Cracker - Placeholder 
        elif value == 2:
            ClearScreen()
            PrintMessage("Fern Wifi Cracker Placeholder")
            input("\nPress enter to continue.")

        # Selection: 10 - Opens the IP Info applet 
        elif value == 10:
            IPInfo()

    # If the user enters something they"re not supposed to
    except ValueError:
        try:
            value = float(userInput)
            PrintMessage("You're really trying to break my program. Please stop.", "Error")
            UserInput()

        except ValueError:
            PrintMessage("Please enter a number, not a string.", "Error")
            UserInput()

# Network information applet
def IPInfo():
    netInfo = []
    # Returns a list of network names and IP addresses
    # List indexes:
    # 0 = hostname
    # 1 = private IP address
    # 2 = public IP address
    def GetIP():
        # Get the hostname of the computer
        hostname = socket.gethostname()
        # Get the private IP address starting with "192.168."
        privateIP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip.startswith("192.168.")][:1]
        # Get the public IP address
        publicIP = get("https://api.ipify.org").text
        netInfo.insert(0, hostname)
        netInfo.insert(1, privateIP[0])
        netInfo.insert(2, publicIP)

    ClearScreen()
    GetIP()
    title = open(os.path.join(titleDir, "title-ipinfo.txt"))
    PrintMessage(title.read(), "none", Color.BrightCyan)
    PrintMessage("Your computer name is: " + netInfo[0])
    PrintMessage("Private IP address is: " + netInfo[1])
    PrintMessage("Public IP address is: " + netInfo[2])
    input("\nPress enter to continue.")
    
# Fixes a weird bug in Windows command line to allow printing of colors. 
ClearScreen()

while True:
    MainDashboard()