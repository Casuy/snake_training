
ssd_train = open("ssd_train.txt","w")
ssd_test = open("ssd_test.txt","w")
classes = ["BandyBandy", "CarpetPython", "CoastalTaipan", "CommonDeathAdder", "EasternBrownSnake",
           "LowlandCopperhead", "MulgaSnake", "RedBelliedBlackSnake", "SpottedPython",
           "TigerSnake", "WesternBrownSnake"]

with open("./train.txt","r") as f:
    allfile = f.readlines()
    for file in allfile:
        name,xmin,ymin,xmax,ymax,label = file.split(",")
        label_index = classes.index(str(label).strip())
        ssd_train.write(name+"***"+xmin+","+ymin+","+xmax+","+ymax+","+str(label_index))
        ssd_train.write("\n")

# with open("./test.txt","r") as f:
#     allfile = f.readlines()
#     for file in allfile:
#         name,xmin,ymin,xmax,ymax,label = file.split(",")
#         label_index = classes.index(str(label).strip())
#         ssd_test.write(name+"***"+xmin+","+ymin+","+xmax+","+ymax+","+str(label_index))
#         ssd_test.write("\n")
# ssd_train.close()
# ssd_test.close()
# import os
os.remove("./train.txt")
#os.remove("./test.txt")