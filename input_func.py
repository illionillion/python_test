print('名前を入力してください')
val_name=input()

print('年齢を入力してください')
val_age=input()
print(val_age.isdigit())
while not val_age.isdigit():#notで否定

  print('数値が入力されていません')
  print('年齢を入力してください')
  val_age=input()

print('こんにちわ、'+val_age+'歳の'+val_name+'さん')
import os
path='./txt/'+val_name+'.txt'
f=open(path,'w',encoding='utf-8')#encoding='utf-8'文字コード指定
f.write('名前:'+val_name+'\n'+'年齢:'+val_age+'')#名前:、年齢:と日本語にしたらVScodeで見る時に文字化けるメモ帳なら文字化けしない
f.close()
