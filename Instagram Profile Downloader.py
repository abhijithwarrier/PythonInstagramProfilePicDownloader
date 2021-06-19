# Programmer - python_scripts (Abhijith Warrier)

# A PYTHON GUI TO DOWNLOAD & SHOW PREVIEW OF PROFILE PICTURE OF THE USER-INPUT INSTAGRAM ID USING INSTALOADER LIBRARY

# Instaloader is a tool to download pictures (or videos) along with their captions and other metadata from Instagram.
# Instaloader exposes its internally used methods and structures as a Python module, making it a
# powerful and intuitive Python API for Instagram, allowing to further customize obtaining media and metadata.
#
# The module can be installed using the command - pip install instaloader

# Importing necessary packages
import os
import instaloader
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    urlLabel = Label(root, text="INSTAGRAM ID : ", background = "deepskyblue4")
    urlLabel.grid(row=0, column=0, padx=5, pady=5)

    root.urlEntry = Entry(root, width=30, textvariable=insta_id)
    root.urlEntry.grid(row=0, column=1,columnspan=2, pady=5)

    dwldBTN = Button(root, text="DOWNLOAD", command=i_Downloader)
    dwldBTN.grid(row=0, column=3, padx=5, pady=5)

    root.resultLabel = Label(root, textvariable=dwldtxt, background = "deepskyblue4")
    root.resultLabel.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
    root.resultLabel.config(font=("Courier", 25))

    root.previewLabel = Label(root, text="DP PREVIEW : ", background = "deepskyblue4")
    root.previewLabel.grid(row=3, column=0, padx=5, pady=5)

    root.dpLabel = Label(root, background = "deepskyblue4")
    root.dpLabel.grid(row=4, column=1, columnspan=2,padx=1, pady=1)

# Defining i_Downloader() to download the INSTAGRAM PROFILE PICTURE
def i_Downloader():
    # Storing the path where to download the instagram profile picture in d_path variable
    d_path = "YOUR'S PREFERRED DOWNLOAD LOCATION"
    # Fetching the user-input instagram id
    insta_username = insta_id.get()

    # Creating an object of Instaloader class of instaloader library.
    # Setting the dirname_pattern to custom download location instead of using default download location
    insta_obj = instaloader.Instaloader(dirname_pattern=d_path)
    # Profile picture can be downloaded using the download_profile() method of Instaloader Object
    # First argument passed to the download_profile() is Instagram User ID
    # Setting parameter profile_pic_only to True will download only the profile picture of the specified ID
    insta_obj.download_profile(insta_username, profile_pic_only=True)
    # download_profile() will download some files in addition to the jpg file.
    # Fetching filename of the JPG File by filtering the files in the directory based on the Name that
    # starts with the Instagram User ID and ends with .jpg extension.
    # JPG FileName Format: python_scripts_2019-10-23_17-07-19_UTC_profile_pic.jpg
    img_name = [img for img in os.listdir(d_path) if img.startswith(insta_username) and img.endswith('.jpg')]

    # Constructing the complete Image Name by concatenating the download path with the image name
    complete_image_name = d_path+"/"+img_name[0]
    # Opening the image using the open() method of Image Module of Python
    dp_image = Image.open(complete_image_name)
    # Resizing the image using Image.resize()
    dp_image = dp_image.resize((200, 200), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    image = ImageTk.PhotoImage(dp_image)
    # Configuring the label and displaying the image
    root.dpLabel.config(image=image)
    root.dpLabel.photo = image
    # Displaying success message
    dwldtxt.set('DP DOWNLOADED SUCCESSFULLY')

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color disabling
# the  resizing property of the tkinter window
root.geometry("510x350")
root.title("InstagramDP DOWNLOADER")
root.config(background = "deepskyblue4")

# Creating tkinter variable
insta_id = StringVar()
dwldtxt = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
