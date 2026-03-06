from core.lexer import tokenize
from core.parser import Parser
from core.compiler import Compiler
from core.vm import VirtualMachine

# The high-level code we want to 'compile'
code = "x = 10 + 20"

# 1. Break into tokens
tokens = tokenize(code)

# 2. Build the Tree
ast = Parser(tokens).parse()

# 3. Generate Instructions
bytecode = Compiler().compile(ast)

# 4. Run the Machine
result = VirtualMachine().run(bytecode)

print(f"Compilation and Execution Successful!")
print(f"Final State of Variables: {result}")