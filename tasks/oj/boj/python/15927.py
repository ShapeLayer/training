# * 전체가 팰린드롬
#  - 길이 - 1
#  - 모두 같은 문자로 팰린드롬: -1
# * 전체가 팰린드롬이 아님

gets = input()

is_palindrome = True
for i in range(len(gets)//2):
    if gets[i] != gets[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    c_init = gets[0]
    for c_now in gets[1:]:
        if c_init != c_now:
            print(len(gets) - 1)
            exit()
    print(-1)
else:
    print(len(gets))
