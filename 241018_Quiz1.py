import random

def generate_lotto_numbers():
    result = []

    while len(result) < 6:
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)

    return result

lotto_numbers = generate_lotto_numbers()
print(lotto_numbers)
