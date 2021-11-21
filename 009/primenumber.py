#print all prime numbers

for possible_prime in range(2,10001):
    for num in range(2, possible_prime):
        if (possible_prime % num == 0):
            break
    else:
        print(f"Prime Number: {possible_prime}")