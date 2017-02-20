# 뇌를 자극하는 파이썬 ch 7 참고

# 절대값 변환 함수 설정
def abs(arg):

    if(arg<0):
        result = arg * -1
    else:
        result = arg
    return result

# text print 함수 설정


def print_string(text, count=1):
    for i in range(count):
        print(text)


# arg 변수에 int형태로 인풋 받음
arg = int(input("input"))
print(abs(arg))

# 인풋에 텍스트 카운트 변수에 인트형태로 숫자 받기
text = input("뭐쓸까?")
count = int(input("몇번?"))

# 프린트스트링 함수에 입력하여 print
print(print_string(text,count))

# 가변매개변수 활용 *를 사용하면 튜플로 변수 설햣 
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s
    return result

a = "aaa"
b = "bbb"
c = "ccc"
# a, b, c 변수의 값을 merge string함수에 반영하여 출력
print(merge_string(a,b,c))