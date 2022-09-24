import re
def is_palindrome(x):
    temp_str = re.sub(r'[^a-zA-Z]+', '', x)
    temp_str = temp_str.lower()

    if temp_str == temp_str[::-1]:
        return True
    return False
