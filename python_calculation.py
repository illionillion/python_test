# 加算
print(15+25)

# 減算
print(20-30)

# 乗算
print(2*5*10)

# 不動点少数の除算
print(10/3)

# 切り捨てる除算
print(10//3)

# 剰余
print(10%3)

# 指数
print(2**5)

# 浮動小数点数（指数表記）
print(6.0221409e+23) #eはどういう意味？

# 浮動小数点数（指数表記） →　整数（多倍長整数）
print(float(602214090000000006225920))

# 浮動小数点数（指数表記） →　整数（多倍長整数）
print(int(6.0221409e+23))

# 16進数
print(0xf+5)
print(0xa*0xa/(0xf+5))

# 8進数
print(0o17)

text='abcd'
text+=text

print(text[0])
print(text[1:5])

print('Hello {}'.format('world')) # 文字列の埋め込み

text='programing by {}'.format('python')

print(text)
print(len(text))
print(text.split())
print(list(range(0,5)))
num_list=list(range(0,5))
# num_list[0]=90

print(num_list)

for i in num_list:
  print(i)
  print(num_list[i])