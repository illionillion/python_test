x=10
import os
for y in range(x):
  print(y)
  path='./txt/'+str(y)+'.txt'
  # path=str(y)+'.txt'
  os.remove(path)
  # f=open(path,'w')
  # f.write('')#ファイル作成
  # f.close()
os.rmdir('./txt')