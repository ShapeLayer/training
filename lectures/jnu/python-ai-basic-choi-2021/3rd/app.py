arr = ['Michael', 'Sarah', 'Isabella', 'Ava', 'Kevin', 'Jacob', 'Aiden', 'Emma', 'Joshua', 'Daniel']
print('시나리오 #1 : {}'.format(arr))
arr.sort()
print('시나리오 #2 : {}'.format(arr))
arr.remove('Isabella')
print('시나리오 #3 : {}'.format(arr))
print('시나리오 #4 : {}'.format(arr[0:3]))
arr += ['Landon']
print('시나리오 #5 : {}'.format(arr))
arr.sort(reverse = True)
print('시나리오 #6 : {}'.format(arr))
arr[arr.index('Ava')] = 'Evan'
print('시나리오 #7 : {}'.format(arr))