import os
import sys
import glob

# Changing the data file name
# 안면 -> face

def korean2english(path):
    oList = os.listdir(path)
    nList = []
    for file_name in oList:
        nList.append(file_name.replace('얼굴', 'face'))
    return oList, nList

def changeName(oPath, nPath, oNames, cNames):
    for idx, filename in enumerate(cNames):
        os.rename(oPath+oNames[idx], nPath+filename)

path = 'C:/jhchoi/data_set/ImageEdit/data/training/label/TL_face_original_k/'
nPath = 'C:/jhchoi/data_set/ImageEdit/data/training/label/TS_face_original_e/'

try:
    if not os.path.exists(nPath):
        os.makedirs(nPath)
    else:
        print("Directory of [{}] is existed".format(nPath))
        sys.exit('종료')
except OSError:
    print("Error: Failed to create the directory.")

ori_file_names, new_file_names = korean2english(path)
changeName(path, nPath, ori_file_names, new_file_names)

