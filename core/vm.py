class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.vars = {}

    def run(self, bytecode):
        for instr in bytecode:
            parts = instr.split()
            cmd = parts[0]

            if cmd == "PUSH": 
                self.stack.append(int(parts[1]))
            elif cmd == "ADD": 
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif cmd == "STORE": 
                self.vars[parts[1]] = self.stack.pop()

        return self.vars
