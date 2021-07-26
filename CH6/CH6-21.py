"""세 개의 양의 정수를 입력받아 그 합이 짝수이면 가장 큰 수를 출력하고, 홀수이면 그 냥 그 합을 출력하는 프로그램"""

a=int(input(''))
b=int(input(''))
c=int(input(''))

total=a+b+c
if a>b:
    max=a
    if a>c:
        max=a
    else:
        max=chr
else:
    max=b
    if b>c:
        max=b
    else:
        max=c

if total%2==0:
    print(max)
else:
    print(total)
