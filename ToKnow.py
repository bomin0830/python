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

4. INPUT
    1) int형으로 변수 받는 법
    : a=int(input(''))
    2) 변수 한꺼번에 여러번 쓰는법
    : 있지만 귀찮음, slice 인가 split써서 했는데 굳이 하고싶으면 찾아봐라

5. LIST
    1) LIST의 구성요소 확인
     - in: list의 원소인가를 확인하는 연산자

    2) 리스트가 가진 다양한 기능
     - list.append(): 리스트에 요소추가
     - list.pop(): 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
     - list.index() : 값을 이용하여 위치찾기
     - list.extend([value1,value2]) : 리스트 뒤에 값을 추가
     - list.insert(index,value): 원하는 위치에 값을 추가
     - list.sort(): 값을 순서대로 정렬
     - list.reverse(): 값을 역순으로 정렬
     
6. TUPLE/SET/DICTIONARY
    1) TUPLE
     - tuple의 생성
       : name=(a,b,c)
     - 
    2) SET형
     - name={a,b,c}
     - 많은 자료를 분리하고 활용
     - 중복을 허용하지 않는다
     - 순서가 없다.
    
    3) DICTIONARY 형
     - dictioinary형의 요소는 한 쌍의 key: value로 표현

7. 반복문
    1) While문
        while 조건:
            True_statements 
        조건에 만족하는 동안 True_statements를 반복적으로 수행
     - break 사용
     :  무한루프에서 조건하나를 더달아서 break
    2) for문
        for item in sequence:
            True_statements
     - range()
     : for문에서 특정 범위를 지정
     - list를 활용한 for문 : 리스트의 요소에서 반복
     - 문자열을 활용한 for문 : 문자열을 쪼게서 반복
     
      


    
"""


