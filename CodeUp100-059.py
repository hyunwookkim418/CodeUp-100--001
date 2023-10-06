# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

# 예를 들어 1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면
#         00000000 00000000 00000000 00000001 이고,
# ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

# 예시
# a = 1
# print(~a) #-2가 출력된다.

# 참고
# 컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다.
# 0과 1로만 구성되는 비트단위들로 변환되어 저장되는데,
# 양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 "2의 보수 표현"방법으로 저장된다.

# 양의 정수 5를 32비트로 저장하면, 

# 5의 2진수 형태인 101이 32비트로 만들어져
# 00000000 00000000 00000000 00000101
# 로 저장된다.(공백은 보기 편하도록 임의로 분리)

# 32비트 형의 정수 0은
# 00000000 00000000 00000000 00000000

# 그리고 -1은 0에서 1을 더 빼고 32비트만 표시하는 형태로
# 11111111 11111111 11111111 11111111 로 저장된다.

# -2는 -1에서 1을 더 빼면 된다.
# 11111111 11111111 11111111 11111110 로 저장된다.

# 이러한 내용을 간단히 표현하면, 정수 n이라고 할 때,

# ~n = -n - 1
# -n = ~n + 1 과 같은 관계로 표현할 수 있다.

# 이 관계를 그림으로 그려보면 마치 원형으로 수들이 상대적으로 배치된 것과 같다.

a = int(input())
print(~a)