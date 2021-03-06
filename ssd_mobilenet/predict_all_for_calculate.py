from ssd import SSD
from PIL import Image

from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import cv2
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


ssd = SSD()


with open("./train_data/test.txt", "r") as f:
    lines = f.readlines()
import  time
detect_time = open("accuracy/time.txt", "w")
for line in lines:
    img_name = line.split(",")[:1][0]
    file_name = img_name.split("/")[-1].split(".")[0]
    print(img_name)
    img = Image.open(img_name)
    with open("accuracy/detections/"+file_name+".txt","w") as f:
        starttime = time.thread_time_ns()/10**6 #ms
        r_image = ssd.detect_image(img)
        endtime = time.thread_time_ns() / 10 ** 6  # ms
        detect_time.write(img_name+" "+str(endtime - starttime)+"\n")
        print("==============")
        for tmp in ssd.predict_all:
            f.write(tmp+"\n")
detect_time.close()