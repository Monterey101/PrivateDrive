import tkinter as tk
from tkinter import *
import os

PrivateDriveFilesFolder = "/Users/kristiankocic/Desktop"

root = tk.Tk()

showFiles = False
showUsage = False

searchItem = StringVar()

numberpdf = 0

def run():
    global numberpdf
    for entry in os.scandir(PrivateDriveFilesFolder):
        name = entry.name
        if name.endswith(".pdf"):
            print(name)
            numberpdf += 1
    print(numberpdf)
run()


######################################################################################################
#                                          VIEWING ALL FILES

def showdownloads():
    global PrivateDriveFilesFolder
    PrivateDriveFilesFolder = "/Users/kristiankocic/Downloads"
    print("Looking at Downloads")
    showAllFiles()

def showdocuments():
    global PrivateDriveFilesFolder
    PrivateDriveFilesFolder = "/Users/kristiankocic/Documents"
    print("Looking at Documents")
    showAllFiles()

def showdesktop():
    global PrivateDriveFilesFolder
    PrivateDriveFilesFolder = "/Users/kristiankocic/Desktop"
    print("Looking at Desktop")
    showAllFiles()

def showAllFiles():
    tk.Frame(root, bg="white", width=1300, height=850).place(relx=0.2, rely=0.1)
    tk.Label(previewFiles, text="All Files", font=("Arial", 30), bg="white", fg="black").place(relx=0.25, rely=0.15)
    tk.Button(previewFiles, text="Upload", bg="white", fg="black", height=2, width=3, command=addFile).place(relx=0.9, rely=0.15)
    tk.Button(previewFiles, text="Downloads", bg="white", fg="black", height=2, width=5, command=showdownloads).place(relx=0.6, rely=0.15)
    tk.Button(previewFiles, text="Documents", bg="white", fg="black", height=2, width=5, command=showdocuments).place(relx=0.5, rely=0.15)
    tk.Button(previewFiles, text="Desktop", bg="white", fg="black", height=2, width=5, command=showdesktop).place(relx=0.4, rely=0.15)
    
    counter = 0.3

    with os.scandir(PrivateDriveFilesFolder) as entries:
        for entry in entries:
            tk.Button(previewFiles, text=entry.name, width=70, height=2, anchor="w", padx=20).place(relx=0.25, rely=counter)
            counter+=0.065


######################################################################################################
#                                            FINDING USAGE

def showUsage():
    tk.Frame(root, bg="white", width=1300, height=850).place(relx=0.2, rely=0.1)
    tk.Label(previewFiles, text="Usage", font=("Arial", 30), bg="white", fg="black").place(relx=0.25, rely=0.15)

    tk.Label(previewFiles, text=("Uploaded Items: " + getNumberofFiles()), font=("Arial", 15), bg="white", fg="black").place(relx=0.25, rely=0.3)
    tk.Label(previewFiles, text=("Capacity Used (Name): " + getUsage() + " Bytes"), font=("Arial", 15), bg="white", fg="black").place(relx=0.25, rely=0.37)

def addFile():
    FileArray.append("NewFile.txt")

def getNumberofFiles():
    counter = 0
    for entry in os.scandir(PrivateDriveFilesFolder):
        counter += 1
    return str(counter)

def getUsage():
    counter = 0
    for entry in os.scandir(PrivateDriveFilesFolder):
        counter += len(entry.name)
    return str(counter)


######################################################################################################
#                                           SEARCHING FILES

def searchFiles():
    tk.Frame(root, bg="white", width=1300, height=850).place(relx=0.2, rely=0.1)
    tk.Label(previewFiles, text="Search Results", font=("Arial", 30), bg="white", fg="black").place(relx=0.25, rely=0.15)

    print("Searched: " + searchItem.get())
    
    counter = 0.3
    
    with os.scandir(PrivateDriveFilesFolder) as entries:
        for entry in entries:
            if searchItem.get().lower() in entry.name.lower():
                tk.Button(previewFiles, text=entry.name, width=70, height=2, anchor="w", padx=20).place(relx=0.25, rely=counter)
                counter+=0.065

    if counter == 0.3:
        tk.Label(previewFiles, text="No files found", font=("Arial", 15), bg="white", fg="black").place(relx=0.25, rely=0.3)

FileArray = ["PlaceHolder.txt", "NotRealFile.txt", "ForExampleOnly.txt"]

#Setting window name and size
root.title("Pirvate Drive")
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)


######################################################################################################
#                                               HEADER

#Header Frame
header = tk.Frame(root, bg="light blue", padx=20)
header.place(relwidth=1, relheight=0.1)
#Logo (Private Drive)
title = tk.Label(header, text="Private Drive", font=("Arial", 30), padx=20, bg="light blue", fg="black")
title.pack(side="left")
#Search Bar
searchBarFrame = tk.Frame(header, width=70, padx=20, bg="light blue")
searchBarFrame.pack(side="left")
searchBar = tk.Entry(searchBarFrame, width=70, font=("Arial", 15), bg="white", fg="black", textvariable=searchItem)
searchBar.pack(side="left")
#Search Button
searchButton = tk.Button(header, text="Search", height=(2), width=3, command=searchFiles)
searchButton.pack(side="left")


######################################################################################################
#                                             NAVIGATION

#Navigation Frame
sideNavBar = tk.Frame(root, bg="dark blue")
sideNavBar.place(rely=0.1, relwidth=0.2, relheight=0.9)
#Show Files
showAllFilesButton = tk.Button(sideNavBar, text="Files", font=("Arial", 20), bd=0, command=showAllFiles)
showAllFilesButton.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.2)
#Favourites
#showFavouritesButton = tk.Button(sideNavBar, text="Favourites", font=("Arial", 20), bd=0)
#showFavouritesButton.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.4)
#Usage
showUsageButton = tk.Button(sideNavBar, text="Usage", font=("Arial", 20), bd=0, command=showUsage)
showUsageButton.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.6)


######################################################################################################
#                                              MAIN VIEW

previewFiles = tk.Frame(root, bg="white").pack()





root.mainloop()