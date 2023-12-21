from sys import set_int_max_str_digits
set_int_max_str_digits()

n = 2 ** int(input())
if len(str(n)) <= 4300:
    print(n)
