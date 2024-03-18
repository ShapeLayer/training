scores = {
    ['.'] = 0,
    ['K'] = 0,
    ['k'] = 0,
    ['P'] = 1,
    ['p'] = -1,
    ['N'] = 3,
    ['n'] = -3,
    ['B'] = 3,
    ['b'] = -3,
    ['R'] = 5,
    ['r'] = -5,
    ['Q'] = 9,
    ['q'] = -9
}

score = 0
for _i = 1, 8 do
    gets = io.read()
    for j = 1, #gets do
        score = score + scores[string.sub(gets, j, j)]
    end
end
print(score)
