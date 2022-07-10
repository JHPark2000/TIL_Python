# 자신의 컴퓨터에서 프로그램을 실행하고 생성된 수를 살펴보자. 
# 한 번 이상 실행시켜서 매번 새로운 수가 생성되는지 살펴보자.

import random

def test():
  a = random.random()
  return a

output = test()
print(output)
