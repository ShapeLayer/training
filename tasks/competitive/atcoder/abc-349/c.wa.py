from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    s, t = input().strip(), input().strip().lower()
    t_ptr = 0
    for each in s:
        if each == t[t_ptr]:
            t_ptr += 1
        elif t_ptr == 2 and t[t_ptr] == 'x':
            t_ptr += 1
        if t_ptr == 3:
            break
    
    print('Yes' if t_ptr == 3 else 'No')
