# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/9/27 22:00

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)

sys.path.append(PathProject)