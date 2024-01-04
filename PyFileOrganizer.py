import os
import shutil
import re

img = ('.jpg', '.png','.bmp')
vid = ('.mp4', '.mov', '.avi')
zip_file = ('.zip', '.rar')
ofc = ('.ppt', '.pptx', '.xlsx', '.doc', '.docx', '.cvs','.pdf','.txt')
prg = ('.exe',',py')
com_dict = {'Images':img, 'Videos':vid, 'Zips Documents':zip_file, 'Office Documents':ofc, 'Programs':prg}

def prompt():
    print("Welcome to FileOrganizer created by Nguyen Duong")
    print("Have a folder where you seem to get lost in millions of files?")
    print("Simply enter your directory and we will fix it in less than a second!")
prompt()
dir = input("Please paste the full file path here:  ")
def file_organizer(directory):
    """function takes in a directory and organise all files to their corresponding folder within that directory"""
    common_file = False
    # Add extra “\” to directory
    temp = directory.split('\\')
    i = 0
    while i < len(temp):
        temp[i] = temp[i] + '\\'
        i += 1
    directory = "".join(temp)
    os.chdir(directory)

    # creating folders for common file types
    for key, value in com_dict.items():
        ex_path = os.path.join(directory, key)
        os.mkdir(ex_path)

        """check each file type extension and create a new folder if haven’t already 
        or move the file to their existent folder"""

    for file in os.listdir():
        extension = re.findall(r'[.]\w+', file)
        if not extension:
            continue
        for key, value in com_dict.items():
            if extension[-1] in value:
                ex_path = os.path.join(directory, key)
                shutil.move(file, ex_path)
                common_file = True
        if common_file:
            continue
        else:
            new_folder = os.path.join(directory, 'All ' + extension[-1] + ' files')
            try:
                os.mkdir(new_folder)
            except:
                shutil.move(file, new_folder)
            else:
                shutil.move(file, new_folder)

file_organizer(dir)