def is_palindrome(string):
    return string == ''.join(reversed(string))

string = input(str())

print(is_palindrome(string))
