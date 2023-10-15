# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

n = input()

if n == 'A':
      print('best!!!')
elif n == 'B':
      print('good!!')
elif n == 'C':
      print('run!') 
elif n == 'D':
      print('slowly~') 
else:
    print('what?')
