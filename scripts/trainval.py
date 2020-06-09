import os
import random

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = '/Users/casuy/workplace/data/annotation'
txtsavepath = '/Users/casuy/workplace/data'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/Users/casuy/workplace/data/trainval.txt', 'w')
ftest = open('/Users/casuy/workplace/data/test.txt', 'w')
ftrain = open('/Users/casuy/workplace/data/train.txt', 'w')
fval = open('/Users/casuy/workplace/data/val.txt', 'w')

for i in list:
    name = "data/images/" + total_xml[i][:-4] + ".jpg\n"
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()