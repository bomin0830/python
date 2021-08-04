""" 1이상의 정수를 입력하면 그 수의 약수를 출력해준다for """

n=int(input('적어:'))

for v in range(1,n+130):
    if(n%v==0):
        print(v)


 