

all_files = []
with open("../train_data/test.txt","r") as f:
    all_files = f.readlines()
    for file in all_files:
        filename= file.split(",")[0].split("/")[-1].split(".")[0]
        classname = file.split(",")[-1].strip()
        with open("./groundtruths/"+filename+".txt","w") as ff:
            infos = file.split(",")[1:5]
            result = " ".join(infos)
            ff.write(classname + " " + result+"\n")
