""" 수를 입력받아 그수가 짝수인지 홀수인지 while문의 무한루프, 0은 exit, 5,3,2 숫자 각자 입력 결과가 제도로 출력되는지 """

while(True):
    n=int(input('안냐세요:'))
    if(n%2==0):
        print(n,'은 짝수입니다~')
    elif(n==0):
        break        
    else:
        print(n,'은 홀수입니다~')
