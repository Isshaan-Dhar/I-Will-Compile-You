import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+'),
    ('ASSIGN', r'='),
    ('PLUS',   r'\+'),
    ('ID',     r'[A-Za-z]+'),
    ('SKIP',   r'[ \t]+'), 
]

def tokenize(code):
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':

            yield (kind, value)
