# lists Common and Mutable sequence operations 
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(type(days))
# Tuples implement all of the common sequence operation
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
# dictionary
nico = {
    "name" :"Nico",
    "age" : 29,
    "korean": True,
    "fav_food" : ["Kimchi", "Sashimi"]
}

print(nico)
nico["hadnsome"] = True
print(nico)

# function은 어떤 행동(기능)을 가지고 있고 계속 반복 할 수 있는것.

# python에서는 funcition을 만든다고 하지않음. function을 define(정의)한다고 함.
# 들여쓰기로 함수의 시작과 끝을 판단한다. function - > body로
def say_hello():
    print("hello")
    print("boy")

# say_hello는 버튼이고 ()는 버튼을 누르는 행위
say_hello()

# arguments(인자)
def say_hello(who):
    print("hello", who)

say_hello("nico")

def plus(a, b):
    print(a + b)

plus(2, 5)

def minus(a, b):
    print(a - b)

minus(5, 2)

# default value
def minus(a, b=0):
    print(a - b)

minus(5)

def say_hello(name="anonymous"):
    print("hello", name)

say_hello()
say_hello("noci")
 
# 대부분 define(정의)는 input을 필요로 함

# 함수를 정의할떈 결과물에 집중해야한다.

def p_plus(a,b):
    print(a + b)

def plus(a, b):
    return a + b

p_result = p_plus(2, 3)
r_result = plus(2, 3)

print(p_result, r_result)

def plus(a,b):
    return a + b

plus = plus(2, 3)
print("result:",plus)


# keyword argument
def plus(a, b):
    return a + b
result = plus(b=30, a=1)
print(result)

def say_hello(name, age, are_form, fav_food):
    return f"Hello {name} your are {age} years old you are from {are_form} you like {fav_food}"
    

hello = say_hello(name="nico", age="12", are_form="colombia", fav_food="kimchi")
print(hello)

# if ~ else
def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None
    
print(plus(12, 1.2))

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can`t drink")
    elif age == 18 or age == 19:
        print("you are new to this !")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(18)

# for
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
    print(x)

for i in [1, 2, 3, 4, 5]:
    print(i)


