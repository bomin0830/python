""" 수를 입력받아 그수가 소수인지아니니지 while문의 무한루프, 0은 exit, 5,3,2 숫자 각자 입력 결과가 제도로 출력되는지 """

while(True):
    n=int(input('1입력:'))
    if n==0:
        break
    for i in range(2,n):
        if n%i==0:
            print(n,'은 소수가아닌다')
            break
        if i==n-1:
            print(n,'은 소수이다.')
            break