#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#'''
#	@File    :   netronSetup.py
#	@Time    :   2020/12/08 10:32:20
#	@Author  :   ARCW
#	@Version :   1.0
#	@Contact :   wmx129674@126.com
#	@License :   (C)Copyright 2020-2021
#	@Desc    :   None
#'''

# here put the import lib
import sys, getopt
import os, netron

# In[]




# In[]
if __name__ == '__main__':
    # print(__name__)
    filePath = ''
    opts, args = getopt.getopt(sys.argv[1:],'hf:',['filePath='])
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print("python netronSetup.py -f $MODEL_FILE")
        elif opt in ('-f', '--filePath'):
            filePath = arg
    print(filePath)
    netron.start(os.path.abspath(filePath), browse=True)
    
