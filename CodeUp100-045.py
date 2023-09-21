#정수 3개를 입력받아 합과 평균을 출력해보자.

#참고
#공백으로 구분된 한 줄로 값들을 입력받기 위해서는
#a, b, c = input().split()
#과 같은 방법이 가능하고,

#공백으로 구분해 두 값을 출력하기 위해서는
#print(d, e)
#와 같은 방법이 가능하다.

#잘라낸 값들은 그 값의 특성(정수, 실수, 문자, 문자열 ...)에 따라 명확하게 변환시킨 후 사용하는 것이 좋다.

#python 프로그래밍을 처음 배울 때 좋은 습관(단계)
#1. 입력된 문자열을 정확하게 잘라낸다.(공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)
#2. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. (정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)
#3. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 변수를 이용해 계산을 한다.
#4. 원하는 결과 값을 필요한 형태로 만들어 출력한다.(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)

a, b, c = map(int, input().split())
d = (a + b+ c)
e = d/3
print(d, format(e, ".2f"))