class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens) # The list from the Lexer
        self.pos = 0

    def parse(self):
        """Builds a simple dictionary representing the 'Tree'."""
        var_name = self.tokens[self.pos][1] # Get 'x'
        self.pos += 2 # Skip 'x' and '='
        left = self.tokens[self.pos][1] # Get '10'
        self.pos += 1
        op = self.tokens[self.pos][1]   # Get '+'
        self.pos += 1
        right = self.tokens[self.pos][1] # Get '20'
        
        return {"name": var_name, "left": left, "op": op, "right": right}