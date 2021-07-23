x=10
import os
for y in range(x):
  print(y)
  path='./txt/'+str(y)+'.txt'
  if(os.path.isfile(path)):
    os.remove(path)
if not os.listdir('./txt'):
  os.rmdir('./txt')