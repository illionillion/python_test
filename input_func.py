# print("値を入力してください。")
# val=input()
# print(val+"が入力されました")
print('名前を入力してください')
val_name=input()

print('年齢を入力してください')
val_age=input()
print(val_age.isdigit())
while not val_age.isdigit():#notで否定

  print('数値が入力されていません')
  print('年齢を入力してください')
  val_age=input()
else:
    if(val_age.isdigit()):
      print('こんにちわ、'+val_age+'歳の'+val_name+'さん')
      import os
      path='./txt/'+val_name+'.txt'
      f=open(path,'w')
      f.write('名前:'+val_name+'\n'+'年齢:'+val_age+'歳')
      f.close()

      

# if(val_age.isdigit()):
#   print('こんにちわ、'+val_age+'歳の'+val_name+'さん')  
# else:
#   print('数値が入力されていません')