<<<<<<< HEAD
#!/usr/bin/python3
def print_last_digit(number):
    for last_digit in number:
        if number >= 0:
            last_digit = number % 10
            print(f"{:02d}".format(number), end="")
        else:
            last_digit = number % -10
            print(f"{:02d}".format(number), end="")
=======
#!/usr/bin/python3
def print_last_digit(number):
    for last_digit in number:
        if number >= 0:
            last_digit = number % 10
            print(f"{last_digit}", end="")
        else:
            last_digit = number % -10
            print(f"{last_digit}", end="")
>>>>>>> 48d60dc90b5f6616ed679420839feb22689d8f99
