import ply.lex as lex


# Tokens List
tokens = (
    'OPEN_TAG', 'CLOSE_TAG',
    'DNUMBER', 'LNUMBER',
    'VARIABLE',
    'PRINT', 
    'ECHO', 
    'WHILE', 'IF', 'ELSE',
    'CONSTANT_ENCAPSED_STRING', 
    'COMMENT', 
    'PLUS_EQUAL', 'MINUS_EQUAL', 'MUL_EQUAL',
    'DIV_EQUAL', 'MOD_EQUAL', 'POW_EQUAL',
    'GREATEREQUAL', 'LESSEQUAL',
    'EQUAL','NOTEQUAL',
    'GREATER', 'LESS',
)

# --- Multi-character Operators and Tags ---
# Functions are used to ensure these are matched before single-character literals

# PHP Tags
def t_OPEN_TAG(t):
    r'<\?php'
    return t

def t_CLOSE_TAG(t):
    r'\?>'
    return t

# Comparison operators
def t_GREATEREQUAL(t):
    r'>='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

# Single-char comparison operators
t_GREATER = r'>'
t_LESS = r'<'

# Assignment operators
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_MUL_EQUAL = r'\*='
t_DIV_EQUAL = r'/='
t_MOD_EQUAL = r'%='
t_POW_EQUAL = r'\*\*='

# Numbers
def t_DNUMBER(t):
    r'(\d+\.\d+)|(\d+\,\d+)'
    t.value = float(t.value.replace(',', '.'))
    return t

def t_LNUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Variables (like $var, $_var, $var123)
t_VARIABLE = r'\$((_[A-Za-z0-9]\w*)|([A-Za-z]\w*))'

# Keywords (case-insensitive)
t_PRINT = r'[pP][rR][iI][nN][tT]'
t_ECHO  = r'[eE][cC][hH][oO]'
t_WHILE = r'[wW][hH][iI][lL][eE]'
t_IF    = r'[iI][fF]'
t_ELSE  = r'[eE][lL][sS][eE]'

# Strings: single or double quoted
t_CONSTANT_ENCAPSED_STRING = r'(\"([^\\"]|\\.)*\")|(\'([^\\\']|\\.)*\')'

# Comments 
def t_COMMENT(t):
    r'(\#.*)|(//.*)|(\/\*[\s\S]*?\*\/)'
    pass

# Literals (single-character operators and delimiters)
literals = ['+', '-', '*', '/', '=', '(', ')', '.', ';', '{', '}', '%']

# Track line numbers
def t_newline(t): 
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore spaces, tabs, and carriage returns
t_ignore = ' \t\r'

# Error handling
def t_error(t): 
    print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    test_data = r'''
    <?php
    // Testing arithmetic and assignment
    $num1 = 10.5;
    $num2 = 20;
    $num1 += 5;
    
    /* Testing loops and 
       conditionals */
    WHILE ($num2 >= 10) {
        IF ($num2 == 15) {
            PRINT "Midpoint reached";
        } ELSE {
            ECHO 'Counting down...';
        }
        $num2 = $num2 - 1;
    }
    ?>
    '''
    
    lexer.input(test_data)
    for tok in lexer:
        print(tok)