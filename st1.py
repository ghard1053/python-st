
weight = float(input("kg"))
height = float(input("cm"))

height = height / 100
bmi = weight / (height * height)

result = ""
if bmi < 18.5:
    result = "thin"
if (18.5 <= bmi) and (bmi < 25):
    result = "normal"
if (25 <= bmi) and (bmi < 30):
    result = "puti hard"
if bmi >= 30:
    result = "hard"

print("BMI: ", bmi)
print("result: ", result)



fruits = ["apple", "orange", "banana"]
for i, v in enumerate(fruits):
    print(i, v)

list(enumerate(fruits))


prices = {'banana': 300, 'orange': 200, 'apple': 500}
list(prices.keys())
sorted (prices.keys())


fmt = "| {0:<7} | {1:>4} | {2:>5}"
print(fmt.format(name, v, diff))


counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k, v in sorted(counter.items()):
    if v >= 3:
        print(k, v)


s = "abcdefg"
s[1:4]
# 'bcd'
s[2:3]
# 'c'

n = "0123456789"
n[2:5] # '234'
n[4:9] # '45678'
n[5:8] # '567'
m[3:3] # ''

n = "0123456789"
n[:3] # '012'
n[7:] # '789'
n[-1] # '9'
n[-3:] # '789'

n[0:9:2] # '02468'
m[::3] # '0369'

def mul(a, b):
    '''乗算'''
    return a * b

help(mul)


for i in range(10):
    print("hello", i)

def say_hello(i):
    if i <= 0:
        return
    print("hello", i)
    say_hello(i-1)
say_hello(10)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(3))


def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v
print(sumArgs(1, 2, 3))
# タプル

def print_args(**args):
    print(args)
print_args(a=30, b=40, c=50)
# 辞書型


def mul_func(a, b):
    return a * b

def div_func(a, b):
    return a / b

func = mul_func
result = func(2, 3)

func2 = div_func
result = func2(10, 5)

def add_func(a, b):
    return a + b

def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(mul_func)
result = calc_5_3(add_func)


x2 = lamda x : x * 2
x2(2) # 4
x2(4) # 8

tri = lamda a,b : a * b / 2
tri(13,15)

def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(lamda a, b : a + b)
result = calc_5_3(lamda a, b : a + b)


nums = [1, 3, 5, 7, 9]
x2 = lamda x : x * 2
list(map(x2, nums))

list(map(lamda x : x * 2, nums))

list(filter(lamda x : (x % 2) == 0, nums))
list(filter(lamda x : (x > 5), nums))


faster_list = sorted(
    animal_list,
    key = lamda animal : animal[1],
    reverse = True
)

li sorted(
    animal_dict.items(),
    key = lamda x : x[1],
    reverse = True
)

