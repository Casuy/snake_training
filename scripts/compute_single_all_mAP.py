from voc_eval import voc_eval
import re
import os

results_path = os.path.abspath("/Users/casuy/workplace/data/result")
sub_files = os.listdir(results_path)

mAP = []
for i in range(len(sub_files)):
    class_name = sub_files[i].split(".txt")[0]
    rec, prec, ap = voc_eval('/Users/casuy/workplace/data/result/{}.txt',
                             '/Users/casuy/workplace/data/annotation/{}.xml',
                             '/Users/casuy/workplace/data/val_name.txt', class_name, '.')
    print("{} :\t {} ".format(class_name, ap))
    mAP.append(ap)

mAP = tuple(mAP)
