"""Task-Given a array of positive integers with name digits.
   imagine digits presents an integer your task is to add one to that integer
   Example:
   digits = [1, 2, 3]
   output - [1, 2, 4]"""



digits = [9, 9, 9]

answer = 0

def plus_one(l, res):
    for i in l:
        res = (res * 10) + i
    res += 1
    return [i for i in str(res)]

answer = plus_one(digits, answer)

print(answer)