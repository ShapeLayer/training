import requests
from json import loads, dumps
import os
from collections import deque
import datetime

C = {
    'solved_api': 'https://solved.ac/api/v3/problem/lookup?problemIds={problem_id}',
    'solved_badge': 'https://static.solved.ac/tier_small/{level}.svg',
    'ext_links': 'extensionlinks.json',
    'dirignore': '.dirignore',
    'path_offset': '../../',
    'root_offset': './',
    'readme_template': 'template.md',
    'cache': 'cache.json'
}
EXT_LINKS = loads(open(C['ext_links']).read())
IGNORES = open(C['dirignore']).read().split('\n')
TABLE = open(C['readme_template']).read()
TABLE_BODY = '''
  <tr>
    <td>{badge} {id} {title}</td>
    <td>{links}</td>
  </tr>
'''

def get(src: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(src, headers=headers)
    return res.text if res.status_code == 200 else None

def get_rating(ids: list) -> dict:
    '''
    반환값
    {
        "id" : {
            "id": 0
            "title": "title",
            "level": 0
        },
        ...
    }
    '''
    res = get(C['solved_api'].format(problem_id=','.join(ids)))
    if not res:
        return
    lookups = loads(res)
    content = {'hello': 'hello'}
    for lookup in lookups:
        content[lookup['problemId']] = {
            'id': lookup['problemId'],
            'title': lookup['titleKo'],
            'level': lookup['level']
        }
    print(True)
    print(content)
    return content

def chk_structure(target: str) -> int:
    '''
    인자값
    target: 대상 언어 ID (ext_links의 인덱스 키)

    반환값
    0: 문제가 1천 단위로 나눠서 저장되어있지 않음
    1: 문제가 1천 단위로 나눠서 저장되어있음
    '''
    set_ = set()
    for f in os.listdir(C['path_offset'] + target):
        for i in f.split('.'):
            set_.add(i)
    if EXT_LINKS[target]['ext'] in set_:
        return 0
    else:
        return 1

def problem_index(target: str) -> list:
    '''
    인자값
    target: 대상 언어 ID (ext_links의 인덱스 키)

    반환값
    {'1000': ['lang_id(=target)', 'filepath'], ...}
    '''
    problems = {}
    langdir = C['path_offset'] + EXT_LINKS[target]['dir']
    queue = deque()
    if chk_structure(target) == 1:
        for f in os.listdir(langdir):
            if os.path.isdir(langdir+f):
                queue.append(f)
    else:
        queue.append('')
    while queue:
        dir_offset = queue.pop()
        dir_offset += '/' if dir_offset != '' else ''
        for f in os.listdir(langdir+dir_offset):
            if f.split('.')[-1] == EXT_LINKS[target]['ext']:
                problem_id = f.split('.')[0]
                path = C['root_offset'] + EXT_LINKS[target]['dir'] + dir_offset + f
                if problem_id in problems:
                    problems[problem_id] += [[target, path]]
                else:
                    problems[problem_id] = [[target, path]]
    return problems

def update_cache(problems):
    cache = loads(open(C['cache']).read())
    problems_cache = cache['problems'].keys()
    arr = []
    for problem in problems:
        if problem not in problems_cache:
            arr += [problem]
    ratings = get_rating(arr)
    print(ratings)
    print(True)
    cache['problems'].update(ratings)
    cache['latest-update'] = str(datetime.datetime.now())
    with open(C['cache'], 'w', encoding='utf-8') as f:
        f.write(dumps(cache, ensure_ascii=False, indent=2))

def get_from_cache():
    cache = loads(open(C['cache']).read())

if __name__ == '__main__':
    langs = os.listdir(C['path_offset']) # 'boj' directory
    problems = {}
    for lang in langs:
        if lang in IGNORES:
            continue
        problems.update(problem_index(lang))
    update_cache(problems.keys())
