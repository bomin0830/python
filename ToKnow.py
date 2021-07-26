"""파이썬 문법 할때 알아둬야 할 것들을 적어보자"""
"""
1. 연산자
    1) +,-,*,/
    2) % : 나머지
    3) //: 몫
    4) **:제곱
2. 복합대입 연산자
    1) a+=1 -> a=a+1
    2) a-=1 -> a=a-1
    3) a*=1 -> a=a*1
    4) a/=1 -> a=a/1
    5) a//=1 -> a=a//1
    6) a%1=1 -> a=a%1

3. 자료형
    1) 자료형 반환 함수 : type(argument)
    2) string의 일부분 추출(slice)
     - [n:m] = n번째부터 m번째 사이의 부분, n은 포함하고, m은 뺀 부분을 지정, (m-n)길이의 문자(열) 생성

4. LIST
    1) 길이 재기 : len(리스트명)
    2) slice 연산
     - list_name[index1:index2]
     - list_name[:] = 모든 범위의 list를 생성하는 연산
     - list_name[:index2] = index2 미만(index2-1)인 범위의 부분list를 생성하는 연산
     - list_name[index1:] = index1 이상 범위의 부분 list를 생성하는 연산
    3) index가 음수인 경우
    : index는 끝에서 부터 센다 -1은 제일 마지막 리스트 요소
"""


