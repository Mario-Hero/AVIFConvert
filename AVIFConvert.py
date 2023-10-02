#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 20.05.2023, Shenzhen
# My Github site: https://github.com/Mario-Hero

import sys
import os
import subprocess


SIZE_CUT = 2.5  # unit:MB. When picture files are larger than SIZE_CUT MB, the script will convert them into avif format.
SIZE_CUT_B = SIZE_CUT * 1024 * 1024

devNull = open(os.devnull, 'w')

def isPic(name):
    namelower = name.lower()
    return namelower.endswith("jpg") or namelower.endswith("jpeg") or namelower.endswith("png")

def compress(folder):
    if os.path.isdir(folder):
        file_list = os.listdir(folder)
        for file in file_list:
            temp = os.path.join(folder, file)
            compress(temp)
    else:
        if isPic(folder):
            if os.path.getsize(folder) > SIZE_CUT_B:
                newName = os.path.splitext(folder)[0] + ".avif"
                if(os.path.exists(newName)):
                    return
                else:
                    if subprocess.call(["avifenc.exe","-s", "10" , "-q", "83", folder, newName], stdout = devNull) == 0:
                        # the quality is set to 83%, which is good enough for pictures.
                        print(folder + " - Success")
                        os.remove(folder)
                    else:
                        print(folder + " - Fail")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for inputFolder in sys.argv[1:]:
            compress(inputFolder)
    # os.system("pause")