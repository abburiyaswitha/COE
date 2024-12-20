def is_valid_password(password):
    if len(password)<10 or len(password)>15:
        return "Password must be between 10 and 15 characters"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    elif not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    elif not any(char in "!@#$%^&" for char in password):
        return "Password must contain at least one special character"
    elif " " in password:
        return "Password should not contain spaces"
    elif password.endswith('.') or password.endswith('@'):
        return "Password should not end with '.' or '@' symbol."
    return "Password is valid!"
password=input("Enter your password:")
print(is_valid_password(password))