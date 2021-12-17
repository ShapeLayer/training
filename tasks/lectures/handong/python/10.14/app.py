# 1
print('XXX 병원 온라인 예약 시스템')
# 2
res_date = []
pat_name = []
sym_data = []
# 4
def new_reservation():
    global res_date, pat_name, sym_data
    # 3
    print('-'*20, '신규 예약', '-'*20)
    ## A
    puts = input('Date (MMDD): ')
    while not puts.isdecimal() or len(puts) != 4 or puts in res_date:
        if puts in res_date:
            print('Already fulled.')
        else:
            print('Wrong Date format')
        puts = input('Date (MMDD): ')
    res_date += [puts]
    # 5
    puts = puts = input('Patient Name: ')
    while len(puts) < 2:
        print('The name must be at least 2 characters long.')
        puts = input('Patient Name: ')
    pat_name += [puts]
    # 6
    sym_data += [input('Symptom: ')]
    # 7
    return True if input('-'*40+'Another reservation? (y) ') == 'y' else False

if __name__ == '__main__':
    # 7
    while new_reservation():
        pass
    # 8
    print('-'*20, '예약 목록', '-'*20)
    # 9
    for i in range(len(res_date)):
        print('+++ Item {} +++'.format(i+1))
        print('Date: {}'.format(res_date[i]))
        print('Patient Name: {}'.format(pat_name[i]))
        print('Symptom: {}'.format(sym_data[i]))
    