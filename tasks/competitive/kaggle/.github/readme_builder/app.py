from os import listdir
from os.path import isdir

# Init
config = {
    'ignore.files': True,
    'path.progress_target': '../../',
    'path.template': 'template.md',
    'path.output': '../../README.md',
    'placeholders': {
        'dir_list': {
            'holder': '{dir_list}'
        }
    }
}

d = config['path.progress_target']

# Load directory list
dirs = []
for _dir in listdir(d):
    if not _dir.startswith('.'):
        dirs.append(_dir)

# Build README
template = open('template.md', encoding='utf-8').read()

buf = []
for each in dirs:
    if config['ignore.files']:
        if not isdir(f'{d}{each}'):
            continue
    buf.append(' * [{display}]({path})'.format(
        display=each.replace('-', ' ').replace('__', ' - '),
        path=f'./{each}'
    ))
template = template.replace(
    config['placeholders']['dir_list']['holder'],
    '\n'.join(buf)
)

# Write to file
with open(config['path.output'], 'w', encoding='utf-8') as f:
    f.write(template)
