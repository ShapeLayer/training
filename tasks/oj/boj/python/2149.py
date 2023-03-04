keys = input()
string = input()
dict_ = {key: [] for key in set(keys)}

v = {key: 0 for key in set(keys)}
loop = 0
offset = len(string)//len(keys)
for key in sorted(keys):
    dict_[key] += [string[loop*offset:(loop+1)*offset]]
    loop += 1

body = ''
for i in range(offset):
    v = {key: 0 for key in set(keys)}
    for key in keys:
        body += dict_[key][v[key]][i]
        v[key] += 1
print(body)
