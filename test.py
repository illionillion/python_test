print("hello world")

import os
dir='./txt'
if not os.path.exists(dir):#()いらない
  os.mkdir('./txt')#フォルダの作成

x=10
for y in range(x):
  print(y)
  path='./txt/'+str(y)+'.txt'
  # path=str(y)+'.txt'
  f=open(path,'w')#ファイル作成
  f.write(str(y))
  f.close()

from math import pi
print(pi)
# 