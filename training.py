import glob
import os
import shutil
import numpy as np

data_image_path="data/images/"

count=0
f = open("train.txt", "w")
fv = open("val.txt", "w")

for img_org_path in glob.iglob(data_image_path + '*'):
    newpath = img_org_path.replace(".PNG", ".png").replace(".JPG", ".jpg").replace(".JPEG", ".jpg")
    if count%10<2:
        fv.write(newpath +"\n")
    else:
        f.write(newpath + "\n")
    shutil.move(img_org_path, newpath)
    count += 1
    print(count)
f.close()
fv.close()
