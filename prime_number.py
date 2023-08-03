n = int(input())
near_prime_number = 0
range_num = n + 2

def is_prime(num):
    for i in range(2, num + 1):
        if i != num and num % i == 0:
            return False
        elif i % num == 0 and num % 1 == 0:
            return True


while near_prime_number == 0:
    for i in range(n + 1, range_num):
        if is_prime(i):
            near_prime_number = i
            break
        else:
            range_num += 1

print(near_prime_number)
