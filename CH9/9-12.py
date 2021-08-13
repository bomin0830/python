""" 양의 정수들의 덧셈인데 0을 입력하면 종료인데 누를거 다더할거임 """
sum=0

while(True):
    n=int(input('아:'))
    sum=sum+n
    if n<=0:
        print('총합은',sum,'입니당')
        break