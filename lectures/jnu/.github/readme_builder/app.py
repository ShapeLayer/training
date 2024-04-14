from sys import argv
import tomli

placeholder = '-'
table_content = [
    '| 항목 | 내용 |',
    '| :-: | :-: |'
]

def build_template(template: str, **kwargs) -> str:
    for key in kwargs:
        template = template.replace(f'##_{key}_##', kwargs[key])
    return template

def load_manifest(_str: str):
    _d = tomli.loads(_str)
    name = _d['name'] if 'name' in _d else placeholder
    code = _d['code'] if 'code' in _d else placeholder
    opened_at = placeholder
    if 'opened_at' in _d:
        opened_at = '-'.join(map(str, _d['opened_at']))
    prof = _d['prof'] if 'prof' in _d else placeholder
    dept = _d['dept'] if 'dept' in _d else placeholder
    return '\n'.join(table_content + [
        f'| 과목명 | { name } |',
        f'| 과목 코드 | { code } |',
        f'| 수강년도 | { opened_at } |',
        f'| 교수 | { prof } |',
        f'| 주관 학과 | { dept } |'
    ]), _d

if __name__ == '__main__':
    if len(argv) < 4:
        raise ValueError('Usage: Python app.py <manifest.toml> <template.md> <output-path>')
    path_manifest = argv[1]
    path_template = argv[2]
    path_output = argv[3]
    content_manifest, parsed_manifest = load_manifest(open(path_manifest, encoding='utf-8').read())
    content_template = build_template(open(path_template, encoding='utf-8').read(),
        name=parsed_manifest['name'],
        summary=content_manifest
    )
    with open(path_output, 'w', encoding='utf-8') as f:
        f.write(content_template)
