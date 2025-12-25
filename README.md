# PHP-Like-Interpreter Compilation Technique Final Project 
This project implements a PHP-like programming language interpreter using Python and PLY (Python Lex-Yacc), with a Streamlit-based UI for interactive execution. The system simulates the core phases of a compiler/interpreter:
- Lexical Analysis (Lexer)
- Syntax Analysis (Parser)
- Semantic Execution (Interpreter)
- Console Execution
- User Interface (Streamlit App)
  
The interpreter supports variables, arithmetic expressions, conditionals, loops, and output statements (print, echo).


### File Structure Explanation
lexer.py	-> Token definitions and lexical rules
parser.py ->	Grammar rules and AST construction
interpreter.py -> Executes AST (semantic evaluation)
app.py	-> Streamlit web application
main.py	-> Console-based runner
test_parser.py	-> Parser testing
test_interpreter.py	-> Interpreter testing
*.php	-> Example PHP-like programs
requirements.txt	-> Project dependencies

**The deployed app can be try here:**
https://php-like-interpreter-group6.streamlit.app/

and can also be tested in console by *python main.py example.php*



