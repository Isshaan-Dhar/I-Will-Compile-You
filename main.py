from core.lexer import tokenize
from core.parser import Parser
from core.compiler import Compiler
from core.vm import VirtualMachine

code = "x = 10 + 20"

tokens = tokenize(code)

ast = Parser(tokens).parse()

bytecode = Compiler().compile(ast)

result = VirtualMachine().run(bytecode)

print(f"Compilation and Execution Successful!")
print(f"Final State of Variables: {result}")
