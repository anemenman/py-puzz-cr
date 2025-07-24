import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


# Example usage:
desired_length = 1025
random_text = generate_random_string(desired_length)
print(f'Generated random string of length {desired_length}: {random_text}')
