class Compiler:
    def compile(self, ast):
        """Translates the AST into a list of low-level instructions."""
        # We push numbers, add them, then store the result in the variable
        return [
            f"PUSH {ast['left']}", 
            f"PUSH {ast['right']}", 
            "ADD", 
            f"STORE {ast['name']}"
        ]