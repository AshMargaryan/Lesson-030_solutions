digits = [9, 9, 9]

answer = 0

def plus_one(l, res):
    for i in l:
        res = (res * 10) + i
    res += 1
    return [i for i in str(res)]

answer = plus_one(digits, answer)

print(answer)