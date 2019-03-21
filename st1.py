
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

