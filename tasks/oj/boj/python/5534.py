n: int = int(input())
name: str = input()
len_name: int = len(name)
ables: list = [input() for _ in range(n)]
ans: int = 0

for able in ables:
    len_able = len(able)
    flag_able = False
    for start in range(len_able):
        if flag_able: break
        if able[start] == name[0]:
            for end in range(start, len_able):
                if flag_able: break
                if able[end] == name[-1]:
                    gap = (end - start - (len_name - 1)) // (len_name - 1) + 1
                    if gap == 0: continue
                    loops = 0
                    flag_case = True
                    for i in range(start, end+1, gap):
                        if able[i] != name[loops]:
                            flag_case = False
                            break
                        loops += 1
                    if flag_case:
                        flag_able = True
    if flag_able:
        ans += 1

print(ans)