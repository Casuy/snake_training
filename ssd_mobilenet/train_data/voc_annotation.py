import xml.etree.ElementTree as ET
from train_data.data_config import get_train_parent

classes = ["Bandy Bandy", "Carpet Python", "Coastal Taipan", "Common Death Adder", "Eastern Brown Snake",
           "Lowland Copperhead", "Mulga Snake", "Red Bellied Black Snake", "Spotted Python",
           "Tiger Snake", "Western Brown Snake"]

def convert_annotation(clss,image_id, list_file):
    in_file = open(get_train_parent()+'annotation/%s/%s.xml'%(clss,image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        if len(b) > 0:
            list_file.write(get_train_parent() + 'images/%s/%s.jpg' % (cls, image_id))
            list_file.write("," + ",".join([str(a) for a in b]) + ',' + str("".join(str(cls).split())))
            list_file.write('\n')

all_test = []
import glob
list_file = open('tmp.txt' , 'w')
for cls in classes:
    imgs = glob.glob(get_train_parent()+"images/"+cls+"/*.jpg")
    for img in imgs:
        filename = img.split("\\")[-1].split(".")[0].strip()
        convert_annotation(cls,filename, list_file)
list_file.close()
import numpy as np
train_data = open("train.txt","w")
test_data = open("test.txt","w")
k = 0
with open("tmp.txt","r") as f:
    allfile = f.readlines()
    np.random.shuffle(allfile)
    for file in allfile:
        if k<50:
            test_data.write(file)
        else:
            train_data.write(file)
        k+=1
train_data.close()
test_data.close()
import  os
os.remove("tmp.txt")

