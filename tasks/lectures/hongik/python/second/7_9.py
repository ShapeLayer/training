from random import randint

display = ['가위', '바위', '보']
rsp_member = ['로미오', '줄리엣']
rsp_result = [randint(0, 2) for _ in range(2)] # [로미오, 줄리엣]

def end(case: int):
    global rsp_member
    if case < 2:
        print('{}{} 이겼습니다.'.format(rsp_member[case], '가' if case == 0 else '이'))
    else:
        print('비겼습니다.')

for i in range(2):
    print('{}의 승부: {}'.format(rsp_member[i], display[rsp_result[i]]))
if rsp_result[0] > rsp_result[1]: # 로미오 승리
    if rsp_result[0] == 2 and rsp_result[1] == 0: # 예외: 로미오 보, 줄리엣 가위
        end(1)
    else:
        end(0)
elif rsp_result[0] < rsp_result[1]: # 줄리엣 승리
    if rsp_result[1] == 2 and rsp_result[1] == 0: # 예외
        end(0)
    else:
        end(1)
else: # 비김
    end(2)
