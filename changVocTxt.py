'''
change .txt file from VOC dataset 2007_test.txt
'''

import os

oldTxtFile = "/home/deepnorth/Disk1T/VOCdevkit/2012_val.txt"
add_dir = "/home/deepnorth/Disk1T"

txtfile = open(oldTxtFile,"r")
newText = open('2012_val.txt', 'w')

for line in txtfile.readlines():
	newline = line[30:]
	newPwd = os.path.join(add_dir, newline)
	print(newPwd)
	newText.write(newPwd)

newText.close()
print("Done!!!!!!!!!!!!")
