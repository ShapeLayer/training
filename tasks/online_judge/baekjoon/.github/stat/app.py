import os
import yaml
import json
import requests
import datetime

CONFIG = {
    'PROCESSING_TARGET_DIR': '../../',
    'BOJ_PROBLEM_URL': 'https://www.acmicpc.net/problem/{id}',
    'SOLVED_QUERY_WITH_ID_ARR': 'https://solved.ac/api/v3/problem/lookup',
    'SOLVED_RANKING_BADGE_URL': 'https://static.solved.ac/tier_small/{problem_level}.svg',
    'SOLVED_RANKING_BADGE_HEIGHT': 13,
    'SOLVED_QUERY_REQUEST_CHUNK_SIZE': 100,
    'LANGUAGES_YML': './languages/languages.yml',
    'LANGUAGES_OVERRIDE': './languages/override.json',
    'IGNORES_FILE': 'ignore',
    'PLACEHOLDER_URL': 'https://img.shields.io/badge/-%20-{color}?style=flat-square',
    'PLACEHOLDER_DEFAULT_COLOR': 'fff',
    'MAKE_FILE_TARGET': '../../README.md',
    'TEMPLATE_FILE': 'template.md'
}
_D = CONFIG['PROCESSING_TARGET_DIR']
LANGUAGES = {}
IGNORE = ''

# Load `languages.yml` and `override.json`
with open(CONFIG['LANGUAGES_YML']) as f:
    LANGUAGES = yaml.load(f, Loader=yaml.FullLoader)
with open(CONFIG['LANGUAGES_OVERRIDE']) as f:
    langs_override = json.loads(f.read())
    for lang in langs_override:
        override_result = {}  
        if 'languages.yml' in langs_override[lang]:
            yaml_base_target = langs_override[lang]['languages.yml']
            override_result = LANGUAGES[yaml_base_target].copy()
        if 'override' in langs_override[lang]:
            override_config = langs_override[lang]['override']
            for key in override_config:
                override_result[key] = override_config[key]
        LANGUAGES[lang] = override_result
IGNORE = open(CONFIG['IGNORES_FILE']).read().split('\n')

# Load code directories
code_dirs = []
for lang_dir in os.listdir(_D):
    if not lang_dir.startswith('.'):
        code_dirs.append(lang_dir)

# Generate key using languages.yml
code_key = {}
for code_dir in code_dirs:
    if code_dir in LANGUAGES:
        code_key[code_dir] = (code_dir)
    elif code_dir[0].upper() + code_dir[1:]:
        code_key[code_dir] = (code_dir[0].upper() + code_dir[1:])

# Load code files
prob_code_file = {}
'''
prob_code_file = {
    1000: [
        {
            'file': 'python/1000.py',
            'lang': 'Python'
        }
    ]
}
'''
for code_dir in code_dirs:
    if code_dir in IGNORE: continue
    now_lang = code_key[code_dir]
    files = os.listdir(f'{_D}{code_dir}')
    for file in files:
        ext = file.split('.')[-1]
        if f'.{ext}' in LANGUAGES[now_lang]['extensions']:
            # init prob_code_file by problem number
            prob = file.split('.')[0]
            if prob not in prob_code_file:
                prob_code_file[prob] = []
            prob_code_file[prob].append( {'file': f'./{code_dir}/{file}', 'lang': now_lang } )

# Get problem information
prob_info = {}
headers = { 'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json' }
## Paginate 100 prob
prob_chunks = []
prob_chunk_size = CONFIG['SOLVED_QUERY_REQUEST_CHUNK_SIZE']
prob_code_file_keys = list(prob_code_file.keys())
for i in range(0, len(prob_code_file), prob_chunk_size):
    prob_chunks.append(prob_code_file_keys[i:i+prob_chunk_size])

for chunk in prob_chunks:
    params = { 'problemIds': ','.join(chunk) }
    res = requests.get(
        url=CONFIG['SOLVED_QUERY_WITH_ID_ARR'],
        params=params,
        headers=headers
    )
    if res.status_code == 200: # 400: Too many problemIds
        for prob in json.loads(res.text):
            prob_id = str(prob['problemId'])
            prob_info[prob_id] = prob
    else:
        print(res)

# Get updatetime
now_kst = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
last_update_time = now_kst.strftime('%Y-%m-%d %H:%M:%S')

# Build string
body = '''
{last_update_time}
<table>
    <tr>
        <th>문제</th>
        <th>코드</th>
    </tr>
    {table_body}
</table>
'''
table_body = []
for prob in map(str, sorted(map(int, prob_code_file.keys()))):
    info = prob_info[prob]
    prob_string = '{badge} {prob_id} {prob_title}'
    badge = '<img src="{url}" height="{height}" />'.format(url=CONFIG['SOLVED_RANKING_BADGE_URL'].format(problem_level=info['level']), height=CONFIG['SOLVED_RANKING_BADGE_HEIGHT'])
    prob_title = info['titleKo']
    prob_string = prob_string.format(badge=badge, prob_id=prob, prob_title=prob_title)
    prob_a = '<a href="{url}" target="_blank" rel="noreferrer noopener">{value}</a>'.format(
        url=CONFIG['BOJ_PROBLEM_URL'].format(id=prob),
        value=prob_string
    )

    files = []
    for file in prob_code_file[prob]:
        color = CONFIG['PLACEHOLDER_DEFAULT_COLOR']
        if 'color' in LANGUAGES[file['lang']]:
            color = LANGUAGES[file['lang']]['color']
        lang_name = file['lang']
        if 'name' in LANGUAGES[file['lang']]:
            lang_name = LANGUAGES[file['lang']]['name']
        files.append('<a href="{path}">{placeholder} {language}</a>'.format(
            path = file['file'],
            placeholder = '<img src="{url}"/>'.format(url=CONFIG['PLACEHOLDER_URL'].format(color=color.replace('#', ''))),
            language = lang_name
        ))

    row_body = '''<tr>
        <td>{prob}</td>
        <td>{files}</td>
    </tr>'''.format(prob=prob_a, files='<br>\n'.join(files))
    table_body.append(row_body)

body = body.format(
    last_update_time=f'마지막 업데이트: {last_update_time}  ',
    table_body='\n'.join(table_body)
)

# Make file
template = open(CONFIG['TEMPLATE_FILE']).read()
with open(CONFIG['MAKE_FILE_TARGET'], 'w', encoding='utf-8') as f:
    f.write(template
        .replace('{statis_table}', body)
    )
