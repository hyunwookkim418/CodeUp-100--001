#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

#참고
#y, m, d = input().split('.')
#과 같이 변수들을 순서대로 나열하면 구분기호를 기준으로 잘라 순서대로 저장한다.

#연도, 월, 일이 닷('.')으로 구분되어 입력된다.

#대시(마이너스 기호)를 구분기호로 사용해서
#일-월-연도로 바꿔 출력한다.

date1 = input("Enter date in the format year.month.day: ")

year, month, day = date1.split('.')
formatted_date = f"{day}-{month}-{year}"
print(formatted_date)

