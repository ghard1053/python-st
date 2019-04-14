
# m進数から10進数に変換
def any2dec(target, m):
    n = len(target) - 1
    sum = 0

    for i in range(len(target)):
        if target[i] == 'A':   num = 10
        elif target[i] == 'B': num = 11
        elif target[i] == 'C': num = 12
        elif target[i] == 'D': num = 13
        elif target[i] == 'E': num = 14
        elif target[i] == 'F': num = 15
        else:                  num = int(target[i])
    
        sum += (m ** n) * num
        n -= 1
    return sum

# 10進数の実数を2進数に変換
def dec2bin_ex(target):
    i = int(target)
    f = target - i

    a = []
    while i != 0:
        a.append(i % 2)
        i = i // 2
    
    a.reverse()

    b = []
    n = 0
    while (f != 0):
        temp = f * 2
        b.append(int(temp))
        f = temp - int(temp)
        n += 1
        if (n >= 10):
            break
    
    return a, b
