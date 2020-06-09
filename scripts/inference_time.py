import sys
import os
from pathlib2 import Path

def write_txt(data,name):
    file_write_obj = open(str(name)+".txt", 'w')
    for var in data:
        file_write_obj.writelines(var)
        # file_write_obj.write('\n')
    file_write_obj.close()

file_path = Path.home()/'Downloads'/'Research-project'/'final'/'All-results'

for i,file  in enumerate(file_path.glob('*/*s.txt')):
    print(file)
    with open(str(file),'r') as f:
        time = []
        for line in f:
            time.append(line.split(' ')[-1])
        write_txt(time,i)

