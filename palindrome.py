def palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
string = input("Enter a string: ")
if palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
