## 함수 선언 부
def add_func(n1, n2) :
    return n1 + n2

def sub_func(n1, n2) :
    return n1 - n2

def gob_func(n1, n2) :
    return n1 * n2

def nanu_func(n1, n2) :
    return n1 / n2

def zegob_func(n1, n2) :
    return n1 ** n2




## 전역 변수부
num1, num2, res = 100, 200, 0



## 메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)

res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)

res = gob_func(num1, num2)
print(num1, "x", num2, "=", res)

res = nanu_func(num1, num2)
print(num1, "/", num2, "=", res)

res = zegob_func(num1, num2)
print(num1, "**", num2, "=", res)
