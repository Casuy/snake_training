import glob
import matplotlib.pyplot as plt
files = glob.glob("../train-log/*.txt" )
all_line = []
for file in files:
    with open(file,"r",encoding="utf-8") as f:
        lline = f.readlines()
        for ll in lline:
            all_line.append(ll)
dict_rpn_cls = {}
dict_rpn_reg = {}
dict_det_cls = {}
dict_det_reg = {}
for line in all_line:
    if line.startswith("Epoch ") and line.find("/")>0 and line.find("saving model")<0:
        index = line.split(" ")[-1].split("/")[0].strip()
        #print(index) #
        dict_rpn_cls[int(index)] = -1
        dict_rpn_reg[int(index)] = -1
        dict_det_cls[int(index)] = -1
        dict_det_reg[int(index)] = -1

    if line.startswith("Loss RPN classifier:")>0:
        value =line.split("Loss RPN classifier:")[-1].strip()
        dict_rpn_cls[int(index)] = float(value)
    if line.startswith("Loss RPN regression:")>0:
        value =line.split("Loss RPN regression:")[-1].strip()
        dict_rpn_reg[int(index)] = float(value)

    if line.startswith("Loss Detector classifier:")>0:
        value =line.split("Loss Detector classifier:")[-1].strip()
        dict_det_cls[int(index)] = float(value)
    if line.startswith("Loss Detector regression:")>0:
        value =line.split("Loss Detector regression:")[-1].strip()
        dict_det_reg[int(index)] = float(value)

test_data_1=sorted(dict_rpn_cls.items(),key=lambda x:x[0])
test_data_2=sorted(dict_rpn_reg.items(),key=lambda x:x[0])
test_data_3=sorted(dict_det_cls.items(),key=lambda x:x[0])
test_data_4=sorted(dict_det_cls.items(),key=lambda x:x[0])

test_data ={}
for item in test_data_1:
    test_data[item[0]] = item[1]

for item in test_data_2:
    test_data[item[0]]  += item[1]
for item in test_data_3:
    test_data[item[0]]  += item[1]
for item in test_data_4:
    test_data[item[0]]  += item[1]
test_data=sorted(test_data.items(),key=lambda x:x[0])
x_axis = []
y_axis =[]
for key,value in test_data:
    x_axis.append(key)
    y_axis.append(value)
plt.title('train loss')
plt.plot(x_axis, y_axis, color='green', label='training loss')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
