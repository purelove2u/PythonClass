def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = sum(a, b)
    return result

# 모듈이 제대로 동작하는지 확인하는 코드
if __name__ == "__main__":
    print(safe_sum(5, "5"))
    print(safe_sum(5, 5))
    print(sum(5, 10.4))

