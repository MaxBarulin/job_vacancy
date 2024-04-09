def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(minimum, maximum):
    prime_numbers = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


min_num = 10
max_num = 30
prime_nums = prime_numbers_in_range(min_num, max_num)
print(prime_nums)
