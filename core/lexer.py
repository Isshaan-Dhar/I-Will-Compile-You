import re

# Each pattern represents a "Token" type
TOKEN_SPEC = [
    ('NUMBER', r'\d+'),        # Matches digits
    ('ASSIGN', r'='),          # Matches the assignment operator
    ('PLUS',   r'\+'),         # Matches the addition operator
    ('ID',     r'[A-Za-z]+'),  # Matches variable names (like x, y)
    ('SKIP',   r'[ \t]+'),     # Ignores spaces and tabs
]

def tokenize(code):
    """Breaks raw text into a stream of identified tokens."""
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP': # We don't need spaces for logic
            yield (kind, value)