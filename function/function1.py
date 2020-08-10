# function(함수)
#%% 함수 정의
def hello():
    print("Hello!!!!!!")


# 함수 사용
hello()


#%% 함수 정의
def hello2():
    return "Hello!!!!!!"


# 함수 사용
print(hello2())
msg = hello2()
print(msg, "Hong!!")


#%% 함수 안에 인수 사용
def add(a, b):
    print(a + b)


add(5, 6)


#%% 함수 안에 인수 사용 / return
def add2(a, b):
    return a + b


print(add2(5, 6))

#%% 가변 인자 : 함수 호출시 인자의 개수가 정해져 있지 않은 경우 사용
def add_many(*args):
    print(args)


add_many(15, 63, 869, 45, 67, 5)
add_many(16)
add_many(27, 35, 36)
add_many()
add_many("abc", "def", "hij")

#%%
def add_many2(*args):
    result = 0
    for i in args:
        result += i
    print(result)


add_many2(15, 63, 869, 45, 67, 5)
add_many2(16)
add_many2(27, 35, 36)
add_many2()


#%% 가변인자를 사용시 주의점
#   가변 매개변수 뒤에는 일반 매개변수가 올 수 없음
#   가변 매개변수는 하나만 사용 가능
def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "add":
        result = 0
        for i in args:
            result += i
    return result


print("덧셈 : ", sum_mul("add", 1, 2, 3, 4, 5))
print("곱셈 : ", sum_mul("mul", 1, 2, 3, 4, 5))

#%%
def args_func(*args):
    for arg in args:
        print(arg)
    for k, v in enumerate(args):
        print(k, v)


args_func(1, 23, 546)
args_func("a", "b", "c")
args_func([2, 3, 45, 67])
args_func((2, 3, 45, 67))
args_func({"name": "hong", "age": 25, "addr": "서울"})

#%% 키워드 매개변수
# **kwargs : 가변 인자들을 딕셔너리 형태로 처리
def args_func2(**kwargs):
    print(kwargs)


args_func2(name="Kim")
args_func2(name="Park", age=10, title="title")
args_func2(name="Cho", name2="min", active="test")


#%%
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(20, 30, "park", "kim")
example_mul(20, 30, "park", "kim", age=25, name="cho")


#%% 기본 매개변수 : 함수를 호출할 때 값이 넘어오지 않으면 기본값으로 처리
def print_n_times(value, n=2):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", n=4)

#%% 다중리턴
def sum_and_mul(a, b):
    return a + b, a * b


print(sum_and_mul(3, 4))  # 결과는 튜플로

#%%
a, b = sum_and_mul(4, 5)  # 결과는 개별 변수에 담김
print(a, " ", b)

#%%
def func_mul(x):
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    # return [y1, y2, y3]
    return (y1, y2, y3)


# list1 = func_mul(10)
# print(list1)
tuple = func_mul(10)
print(tuple)

#%%
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)


say_nick("바보")
say_nick("야호")

# %% 두 개의 인자와 연산자를 받아서 사칙연산을 수행하는
#   FourRules 함수를 작성하시오
def FourRules(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        print("연산자를 확인하세요")
    
x, y = 3, 5
print("{} {} {} = {}".format(x, "+", y, FourRules(x, y, "+")))
print("{} {} {} = {}".format(x, "-", y, FourRules(x, y, "-")))
print("{} {} {} = {}".format(x, "*", y, FourRules(x, y, "*")))
print("{} {} {} = {}".format(x, "/", y, FourRules(x, y, "/")))

# %% 소수 구하기
def primeNum():
    x = int(input("숫자를 입력하세요 : "))
    result = 1
    for i in range(2, x):
        if x % i == 0:
            print("소수가 아님")
            result = 0
            break    
    if result == 1:
        print("소수")
primeNum()