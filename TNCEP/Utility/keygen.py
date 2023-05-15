import random
import string

def generate_user_code(length=8):
    characters = string.ascii_letters + string.digits
    user_code = ''.join(random.choice(characters) for _ in range(length))
    return user_code
