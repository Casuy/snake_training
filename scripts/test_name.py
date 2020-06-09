import re

with open('/Users/casuy/workplace/data/val.txt', 'r') as test_path:
    lines = test_path.readlines()
    test_name = open('/Users/casuy/workplace/data/val_name.txt', 'w')
    for i in range(len(lines)):
        name = re.findall(r"\d", lines[i])
        test_name.write("".join(name) + "\n")

test_path.close()
test_name.close()