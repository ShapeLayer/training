# WIP

from sys import stdin
gets = stdin.readline

n, m = map(int, gets().split())
grid = [[' ' for _i in range(m+1)] for _j in range(n+1)]
mobs, items = 0, 0

pp = [-1, -1] # playerpos

def get_init(lv: int):
    return [20+5*lv, 2+2*lv, 2+2*lv]

for i in range(1, n+1):
    row = gets()
    for j in range(1, m+1):
        if row[j] == '&' or row[j] == 'M':
            mobs += 1
        elif row[j] == 'B':
            items += 1
        elif row[j] == '@':
            pp = [i, j]

moves = list(gets())
objects = {}

for mob in range(mobs):
    get = gets().split()
    name = '##_MOB_{}_##'.format(gets[2])
    grid[int(gets[0])][int(gets[1])] = name
    objects[name] = list(map(int, gets[3:6]))

for item in range(items):
    get = gets().split()
    name = '##_ITEM_{}-{}_##'.format(gets[0], gets[1])
    grid[int(gets[0])][int(gets[1])] = name
    tag = ''
    if gets[2] == 'O':
        tag = gets[2]
    else:
        tag = int(gets[3])
    objects[name] = {
        'type': gets[2], 'tag': tag
    }

movemap = {'U': [-1, 0], 'L': [0, -1], 'D': [1, 0], 'R': [0, 1]}
st = {
    'h': 20, # hp
    'a': 2,  # atk
    'd': 2,  # def
    'l': 1,  # lvl
    'e': 0,  # exp
    'w': 0,  # weapon atk
    'r': 0,  # armor def
    'c': []  # accessories
}

for move in moves:
    dt = movemap[move]
    np = pp + dt
    if np[0] <= 0 or np[0] > n or np[1] <= 0 or np[1] > m or grid[np[0]][np[1]] == '#':
        continue
    now = grid[np[0]][np[1]]
    ##

    ##
    grid[pp[0]][pp[1]] = '.'
    grid[np[0]][np[1]] = '@'
    pp = np
