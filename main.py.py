import re

class MiniCompiler:
    def __init__(self):
        # This acts as our "Memory" or "Symbol Table"
        self.variables = {}

    def compile(self, code):
        # .strip() handles leading/trailing whitespace in the whole block
        lines = code.strip().split("\n")

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip empty lines to prevent errors
            if not line:
                continue

            # Case 1: Variable assignment (e.g., x = 5 + 3)
            if "=" in line:
                var, expr = map(str.strip, line.split("=", 1))
                
                try:
                    # FIX: Pass self.variables as the 'locals' dictionary.
                    # This allows eval to see 'x' when calculating 'y = x * 2'.
                    value = eval(expr, {"__builtins__": None}, self.variables)
                    self.variables[var] = value
                    print(f"STORE {value} -> {var}")
                except NameError as e:
                    print(f"Error on line {line_num}: {e}")
                except Exception as e:
                    print(f"Syntax Error on line {line_num}: {e}")

            # Case 2: Print statement (e.g., print y)
            elif line.startswith("print "):
                # FIX: Using split instead of replace to avoid mangling variable names
                parts = line.split(maxsplit=1)
                if len(parts) > 1:
                    var = parts[1]
                    # Check if the variable exists in our memory
                    if var in self.variables:
                        print(f"OUTPUT {self.variables[var]}")
                    else:
                        print(f"Error on line {line_num}: Variable '{var}' is not defined.")

# --- Execution ---

compiler = MiniCompiler()

program = """
x = 5 + 3
y = x * 2
print y
"""

print("--- Compiling/Interpreting ---")
compiler.compile(program)