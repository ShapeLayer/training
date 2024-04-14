text = input('문자열을 입력하시오 : ').replace(' ', '').lower()
if len(text) % 2 == 1:
    offset = [1, 1]
else:
    offset = [1, 0]
anchor = len(text) // 2

flag = True
for i in range(anchor):
    if not text[anchor-offset[0]-i] == text[anchor+offset[1]+i]:
        flag = False
        break
print('회문입니다.' if flag else '회문이 아닙니다.')
