"""사과는 1000원, 포도는 3000원 배는 2000원 귤은 500원에 파는 과일가게에서 포도를 3송이 이상사면 총금액의 10프로글 ㄹ할인해준다 할때 총 금액을 계산해주는 프로그램을 작성해라"""

apple=1000

grape=3000
pear=2000
mandarine=500

a=int(input('사과: '))
b=int(input('포도: '))
c=int(input('배: '))
d=int(input('귤: '))
total=apple*a+grape*b+pear*c+mandarine*d

if b>=3:
    total=total*0.9
    print('총 금액: ',total)

else:
    print('총 금액: ',total)
