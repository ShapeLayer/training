from sys import stdin
#from sys import #stdout

txt = stdin.readline().rstrip()

cnt = 0
q = ''

def is_able(txt):
    return txt in ['c', 'd', 'l', 'n', 's', 'z']

#i = 0
for t in list(txt):
    #i += 1
    #stdout.write('[{}] {} 처리: '.format(i, t))
    if q: # 이미 감지된 크로아티아 알파벳 시작 문자가 있음
        #stdout.write('Q ')
        if is_able(q):
            #stdout.write('is_able ')
            if (q == 'c' and t == '=') or (q == 'c' and t == '-') or (q == 'd' and t == '-') or (q == 'l' and t == 'j') or (q == 'n' and t == 'j') or (q == 's' and t == '=') or (q == 'z' and t == '='):
                #stdout.write('case-1 ')
                cnt += 1
                q = ''
            elif q == 'd' and t == 'z':
                #stdout.write('case-2 ')
                q += 'z'
            else:
                if is_able(t):
                    #stdout.write('case-3.1 ')
                    cnt += 1
                    q = t
                else:
                    #stdout.write('case-3.2 ')
                    cnt += 2
                    q = ''
        elif q == 'dz':
            #stdout.write('is_dz ')
            if t == '=':
                #stdout.write('case-1 ')
                cnt += 1
                q = ''
            else:
                cnt += 2
                if is_able(t):
                    #stdout.write('case-2.1 ')
                    q = t
                else:
                    #stdout.write('case-2.2 ')
                    cnt += 1
                    q = ''
        else:
            #stdout.write('is_etc ')
            if is_able(t):
                #stdout.write('case-1 ')
                cnt += 1
                q = t
            else:
                #stdout.write('case-2 ')
                cnt += 2
                q = ''
    else: # 이미 감지된 크로아티아 알파벳 시작 문자가 없음
        #stdout.write('NQ ')
        if is_able(t): # 크로아티아 알파벳 시작 문자가 감지됨
            #stdout.write('is_able ')
            q += t
        else: # 크로아티아 알파벳 시작 문자가 감지되지 않음
            #stdout.write('is_etc ')
            cnt += 1
    #stdout.write('result: (cnt: {})'.format(cnt))
    #stdout.write('\n')
if q:
    cnt += len(q)
print(cnt)