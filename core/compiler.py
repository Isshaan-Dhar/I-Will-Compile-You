class Compiler:
    def compile(self, ast):
        return [
            f"PUSH {ast['left']}", 
            f"PUSH {ast['right']}", 
            "ADD", 
            f"STORE {ast['name']}"

        ]
