#benjamin shell

import os, sys

OS = None
directory = "S:\\"
version = "alpha-2"


customCommandList = ["get ip", "trol", "ls"]
customCommandDict = {
    0 : "ipconfig",
    1 : "ping localhost",
    2 : "dir",
}

if sys.version_info < (3, 7):
    print("Sorry but python 3.7 is required")
    sys.quit(input())

if os.name == "nt":
    OS = "windows"
elif OS == None:
    print("Sorry but your Operating System is not supported")
    sys.quit()

print(f"Welcome to the shell\nversion {version}")

while True:
    while True:
        command = input(f"<{os.getlogin()} in {directory}> $ ")
        if "\"" in command:
            print("please use '")
        elif len(command) > 0:
            break
    try:
        if command in customCommandList:
            for x in range(len(customCommandList)):
                if customCommandList[x] == command:
                    command = customCommandDict[x]
                    break
        if directory == "S:\\":
            os.system(f"{command}")
        else:
            command = command.split()
            try:
                b = secondCommand
            except:
                secondCommand = ""
                
            for x in range(len(command)):
                if x > 0:
                    secondCommand += command[x]
            
            os.system(f"{command[0]} {directory}\{secondCommand}")
        if "cd" in command:
            directory += command.split()[1]
    except:
        pass       
