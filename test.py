print("hello world")

x=10
import os
dir='./txt'
if(not os.path.exists(dir)):
  os.mkdir('./txt')#フォルダの作成

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