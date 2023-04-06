gets = ''
while True:
    try:
        gets = input()
    except EOFError:
        break
    print(gets)
