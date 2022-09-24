from PIL import Image
import pillow_heif
import os
import sys
from art import *

art= text2art("Image Converter")

def convert():
    print(art)
    print("1. HEIC to PNG")
    print("2. HEIC to JPEG")
    print("3. PNG to JPEG")
    print("4. JPEG to PNG")
    print("5. Exit")
    userinput = input("Please Select an Option\n")

    if userinput == "1":
        def HEICtoPNG():
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".heic"
            heif_file = pillow_heif.read_heif(img)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".png", format("png"))
            print("Image saved as " + rename + ".png")
        HEICtoPNG()
        convert()

    if userinput == "2":
        def HEICtoJPEG():
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".heic"
            heif_file = pillow_heif.read_heif(img)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".jpeg", format("jpeg"))
            print("Image saved as " + rename + ".jpeg")
        HEICtoJPEG()
        convert()

    if userinput == "3":
        def PNGtoJPEG():
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".png"
            image = Image.open(img)
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".jpeg", format("jpeg"))
            print("Image saved as " + rename + ".jpeg")
        PNGtoJPEG()
        convert()

    if userinput == "4":
        def JPEGtoPNG():
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".jpeg"
            image = Image.open(img)
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".png", format("png"))
            print("Image saved as " + rename + ".png")
        JPEGtoPNG()
        convert()

    if userinput == "5":
        sys.exit()
convert()