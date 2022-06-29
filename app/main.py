def check_password(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            print(1)
            if letter.upper() == letter:
                print(2)
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])
