"""
CP1404/CP5632 Practical
Sort files into subdirectories for each extension Version 1
"""
import os
import shutil

def main():
    extension_to_category = {}
    # Create an os directory for each new extension that program finds
    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

    extension = filename.split('.')[-1]

    if extension not in extension_to_category:
        category = input("What category would you like to sort {} files into? ".format(extension))
        extension_to_category[extension] = category
        # Use exception handling to avoid the crash (just pass)
        try:
            os.mkdir(category)
        except FileExistsError:
            pass

    # Print a list of the extension and filename
    print("{}/{}".format(extension, filename))
    os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))

main()