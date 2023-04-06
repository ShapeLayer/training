'''
# "채점 서버에서 인터넷은 막혀있습니다."
# https://www.acmicpc.net/board/view/11437

from urllib import request
import re
boj_id = 'belline0124'
html = request.urlopen('https://www.acmicpc.net/user/{}'.format(boj_id)).read().decode('utf-8')
print(re.search(re.compile(r'<span id="u-solved">(?P<solved>.*?)<\/span>'), html).group('solved'))
print(boj_id)
'''

print('85\nbelline0124')