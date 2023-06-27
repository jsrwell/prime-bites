import random
import string


def generate_key():
    """Generate Key to Use in Django Settings"""
    characters = string.ascii_letters + string.digits + "!@$%&"
    key = ''.join(random.choice(characters) for _ in range(64))
    blocks = [key[i:i+8] for i in range(0, 64, 8)]
    formatted_key = '-'.join(blocks)
    return formatted_key


print(generate_key())
