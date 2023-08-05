"""Given an integer n. Program must return reversed n.
   Input - 1326
   Output - 6231"""


number = int(input())

def reverse_num(num):
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    return reversed_num

reversed_num = reverse_num(number)
print(reversed_num)