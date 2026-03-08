class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def parse(self):
        var_name = self.tokens[self.pos][1]
        self.pos += 2 # Skip 'x' and '='
        left = self.tokens[self.pos][1]
        self.pos += 1
        op = self.tokens[self.pos][1]
        self.pos += 1
        right = self.tokens[self.pos][1]
        

        return {"name": var_name, "left": left, "op": op, "right": right}
