import doctest


def test(a):
  '''
  test
  簡単な処理

  >>>test()
  200
  '''
  a*=10
  print(a)
  return a

# print(test(20))
if __name__=='__main__':

  test(20)

  # doctest.testmod()#何故かエラる、エラー文読めない