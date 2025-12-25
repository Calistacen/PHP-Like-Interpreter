import sys
from parser import parse
from interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python php.py <source_file.php>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r") as f:
            code = f.read()

        ast = parse(code)

        if ast is None or ast[0] != "PROGRAM":
            raise RuntimeError("Invalid program structure")

        interpreter = Interpreter()
        interpreter.run(ast[1])

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
