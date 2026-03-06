class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.vars = {}

    def run(self, bytecode):
        """Processes each bytecode instruction one by one."""
        for instr in bytecode:
            parts = instr.split()
            cmd = parts[0]

            if cmd == "PUSH": 
                self.stack.append(int(parts[1]))
            elif cmd == "ADD": 
                # Pop the last two numbers, add them, push result back
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif cmd == "STORE": 
                # Save the result from the top of the stack into a variable
                self.vars[parts[1]] = self.stack.pop()
        return self.vars