#시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

#어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.

#시 분 초가 시:분:초 형식으로 입력된다.

#분만 출력한다.

time=input()
split_time = time.split(":")
if len(split_time) > 1:
    minutes = split_time[1]
    print(minutes)
else:
    print("Invalid time format.")