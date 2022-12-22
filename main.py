from PIL import Image
import pillow_heif
import os
import sys
from art import *

art= text2art("Image Converter")

def main():
    print(art)
    print("1. HEIC to PNG")
    print("2. HEIC to JPEG")
    print("3. PNG to JPEG")
    print("4. JPEG to PNG")
    print("5. Exit")
    userinput = input("Please Select an Option\n")

    match userinput:
        case "1":
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
            main()
        case "2":
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
            main()
        case "3":
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".png"
            image = Image.open(img)
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".jpeg", format("jpeg"))
            print("Image saved as " + rename + ".jpeg")
            main()
        case "4":
            im = input("Enter the image name (ex. Pic1): ")
            img = "./" + im + ".jpeg"
            image = Image.open(img)
            rename = input("Enter the new image name (ex. Pic1): ")
            image.save("./" + rename + ".png", format("png"))
            print("Image saved as " + rename + ".png")
            main()
        case "5":
            sys.exit()
        case _: 
            print("Invalid Input")
            main()
main()