import os
import re
from PIL import Image
from xml.etree.ElementTree import parse, Element

directory = os.path.abspath("/Users/casuy/workplace/data/images")
print(directory)

if directory:
    folders = os.listdir(directory)
    print(folders)
    i = 0
    for folder in folders:
        print(i)
        folder_directory = directory + '/' + folder
        print(folder_directory)
        if os.path.isdir(folder_directory):
            files = os.listdir(directory + '/' + folder)
            for file in files:
                if re.match(r'\S+\.jpg', file):
                    print(file)

                    img = Image.open(folder_directory + '/' + file)
                    w = img.width
                    h = img.height
                    print("width: " + str(w) + ", height: " + str(h))

                    temp = file.split('.')
                    annotation_path = '/Users/casuy/workplace/data/annotation/' + folder + '/' + temp[0] + '.xml'
                    print(annotation_path)
                    annotation = parse(annotation_path)
                    root = annotation.getroot()
                    size = root.find("size")
                    width = size.find("width")
                    print("original width: " + width.text)
                    width.text = str(w)
                    print("updated width: " + width.text)
                    height = size.find("height")
                    print("original height: " + height.text)
                    height.text = str(h)
                    print("updated height: " + height.text)
                    annotation.write(annotation_path)


                    print(i)
                    i += 1

