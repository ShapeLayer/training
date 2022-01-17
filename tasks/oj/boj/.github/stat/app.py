from hashlib import new
import requests
from json import loads, dumps
import os
from collections import deque
import datetime
import time
import argparse

parser = argparse.ArgumentParser(description='README Generator')
parser.add_argument('--trace', type=int, default=0, help='set 1 to trace run time')
run_args = parser.parse_args()

C = {
    'boj_problem': 'https://acmicpc.net/problem/{problem_id}',
    'solved_api': 'https://solved.ac/api/v3/problem/lookup?problemIds={problem_id}',
    'solved_badge': 'https://static.solved.ac/tier_small/{problem_level}.svg',
    'placeholder': 'https://via.placeholder.com/{placeholder_size}/{placeholder_color}/000?text=%20',
    'language_color': 'https://raw.githubusercontent.com/ozh/github-colors/master/colors.json',
    'solved_badge_height': 13,
    'placeholder_size': 13,
    'ext_links': 'extensionlinks.json',
    'dirignore': '.dirignore',
    'path_offset': '../../',
    'root_offset': './',
    'readme_template': 'template.md',
    'cache': 'cache.json'
}
EXT_LINKS = loads(open(C['ext_links']).read())
IGNORES = open(C['dirignore']).read().split('\n')
TEMPLATE = open(C['readme_template']).read()
TEMPLATE_BODY = '''
  <tr>
    <td><a href="{boj_problem}"><img src="{badge}" height="{badge_height}"> {problem_id} {title}</a></td>
    <td>{links}</td>
  </tr>
'''#.format(boj_problem = C['boj_problem'], badge = C['solved_badge'])
PROB_CACHE_FORMAT = {
    'latest-update': '',
    'problems': {
    }
}

def debug(fn):
    def wrapper(*args, **kwargs):
        if run_args.trace == 1:
            init = time.time()
            res = fn(*args, **kwargs)
            fina = time.time()
            print('WrokingTime[{}]: {} sec / {} {}'.format(fn.__name__, fina-init, args, kwargs))
        else:
            res = fn(*args, **kwargs)
        return res
    return wrapper

@debug
def get(src: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(src, headers=headers)
    return res.text if res.status_code == 200 else None

@debug
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
    content = {}
    for lookup in lookups:
        content[lookup['problemId']] = {
            'id': lookup['problemId'],
            'title': lookup['titleKo'],
            'level': lookup['level']
        }
    return content

@debug
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

@debug
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

@debug
def update_cache(problems: list) -> None:
    cache = PROB_CACHE_FORMAT
    if os.path.isfile(C['cache']):
        cache = loads(open(C['cache']).read())
        latest_update = datetime.datetime.strptime(cache['latest-update'], '%Y-%m-%d %H:%M:%S.%f')
        if (datetime.datetime.utcnow() - latest_update).days > 14:
            cache = PROB_CACHE_FORMAT
    problems_cache = cache['problems'].keys()
    arr = []
    for problem in problems:
        if problem not in problems_cache:
            arr += [problem]
    for i in arr:
        cache['problems'].update(get_rating([i]))
    cache['latest-update'] = str(datetime.datetime.utcnow())
    with open(C['cache'], 'w', encoding='utf-8') as f:
        f.write(dumps(cache, ensure_ascii=False, indent=2))
@debug
def get_from_cache(problem: str) -> dict:
    cache = loads(open(C['cache']).read())
    return cache['problems'][problem]

if __name__ == '__main__':
    langs = os.listdir(C['path_offset']) # 'boj' directory
    problems = {}
    for lang in langs:
        if lang in IGNORES:
            continue
        getted_problem = problem_index(lang)
        for problem in getted_problem:
            if problem in problems:
                problems[problem] += [getted_problem[problem]]
            else:
                problems[problem] = [getted_problem[problem]]
        problems.update(problem_index(lang))
    update_cache(problems.keys())
    COLOR = loads(get(C['language_color']))
    body = ''
    for problem_int in sorted(list(map(int, problems.keys()))):
        problem = str(problem_int)
        problem_info = get_from_cache(problem)
        links = []
        for file in sorted(problems[problem]):
            language_color = 'fff'
            if file[0] in EXT_LINKS and EXT_LINKS[file[0]]['github-colors'] != '__NONE__':
                language_color = COLOR[EXT_LINKS[file[0]]['github-colors']]['color'][1:]
            links += ['<a href="{src}"><img src="{placeholder}"> {language}</a>'.format(
                src=file[1],
                placeholder=C['placeholder'].format(placeholder_size=C['placeholder_size'], placeholder_color=language_color),
                language=EXT_LINKS[file[0]]['name']
            )]
        body += TEMPLATE_BODY.format(
            boj_problem = C['boj_problem'].format(problem_id=problem),
            badge = C['solved_badge'].format(problem_level=problem_info['level']),
            badge_height = C['solved_badge_height'],
            problem_id = problem,
            title = problem_info['title'],
            problem_level = problem_info['level'],
            links = '<br>'.join(links)
        )
    rendered = TEMPLATE.format(table_body=body)
    with open(C['path_offset']+'README.md', 'w', encoding='utf-8') as f:
        f.write(rendered)