from collections import deque


def is_palindrome(s):

    s = ''.join(char.lower() for char in s if char.isalnum())
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

                
print(is_palindrome("hello"))                        
print(is_palindrome("Was it a car or a cat I saw?"))  
print(is_palindrome("No lemon no melon"))            