while True:
    puts = input()
    if puts == 'end':
        break
    
    accept = True
    vowel_exists = False
    is_vowel = None
    cnt = 0
    for i in range(len(puts)):
        cnt += 1
        if i == 0:
            is_vowel = True if puts[i] in 'aeiou' else False
            vowel_exists = is_vowel
            continue
        
        # cnt init
        now_vowel = True if puts[i] in 'aeiou' else False
        if is_vowel != now_vowel:
            cnt = 1
        is_vowel = now_vowel

        # 1
        if puts[i] in 'aeiou':
            vowel_exists = True
        
        # 2
        if cnt >= 3:
            accept = False
            break
        
        # 3
        if puts[i-1] == puts[i]:
            if puts[i] not in 'eo':
                accept = False
                break

    if not vowel_exists:
        accept = False
    print('<{}> is {}.'.format(puts, 'acceptable' if accept else 'not acceptable'))