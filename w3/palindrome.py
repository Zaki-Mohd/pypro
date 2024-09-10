def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

print("is 'RADAR' palindrome ?",palindrome("RADAR"))
print("is 'NOVON' palindrome ?",palindrome("NOVON"))
print("is 'CLICK' palindrome ?",palindrome("CLICK"))
