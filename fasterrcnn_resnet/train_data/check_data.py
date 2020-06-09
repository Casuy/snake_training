import six
from PIL import Image
import numpy as np
from PIL import Image,ImageFont, ImageDraw
lines = []
with open("./train.txt","r") as f:
    lines = f.readlines()
    np.random.shuffle(lines)
classes = ["Bandy Bandy", "Carpet Python", "Coastal Taipan", "Common Death Adder", "Eastern Brown Snake",
           "Lowland Copperhead", "Mulga Snake", "Red Bellied Black Snake", "Spotted Python",
           "Tiger Snake", "Western Brown Snake"]

for line in lines:
    img_name = line.split(",")[:1][0]
    print(img_name)
    infos = line.split(",")[1:]
    img = Image.open(img_name)

    font = ImageFont.truetype(font='model_data/simhei.ttf',
                              size=np.floor(3e-2 * np.shape(img)[1] + 0.5).astype('int32'))
    draw = ImageDraw.Draw(img)

    xmin, ymin, xmax, ymax, label = infos
    label = str(label).strip()
    label_size = draw.textsize(label, font)
    label = label.encode('utf-8')
    if int(ymin) - label_size[1] >= 0:
        text_origin = np.array([int(xmin), int(ymin) - label_size[1]])
    else:
        text_origin = np.array([int(xmin), int(ymin) + 1])
    for i in range(1):
        draw.rectangle(
            [int(xmin)+i,int(ymin)+i,int(xmax)-i,int(ymax)-i],
            outline =(0,0,255))
    draw.rectangle(
        [tuple(text_origin), tuple(text_origin + label_size)],
        fill=(255,0,255))
    draw.text(text_origin, str(label, 'UTF-8'), fill=(0, 0, 0), font=font)
    img.show()

