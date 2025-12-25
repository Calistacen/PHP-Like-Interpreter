import ply.yacc as yacc
from lexer import tokens

# Precedence of Operator
precedence = (
    ('left', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'EQUAL', 'NOTEQUAL'),
    ('left', '.'),
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
)

# Define program
def p_program(p):
    'program : OPEN_TAG stmt_list CLOSE_TAG'
    p[0] = ('PROGRAM', p[2])

# **STATEMENT LISTS**
def p_stmt_list_multiple(p):
    '''
    stmt_list : stmt_list statement
    '''
    if p[2] is not None:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = p[1]

def p_stmt_list_single(p):
    '''
    stmt_list : statement
    '''
    if p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

# STATEMENTS
def p_statement(p):
    '''
    statement : assignment_statement
              | compound_assignment_statement
              | print_statement
              | echo_statement
              | if_statement
              | while_statement
              | empty_statement
    '''
    p[0] = p[1]


# EMPTY STATEMENTS
def p_empty_statement(p):
    '''
    empty_statement : ";"
    '''
    p[0] = None
    
# Asignment 
def p_statement_assign(p):
    ''' 
    assignment_statement : VARIABLE "=" expression ";"
    '''
    p[0] = ('ASSIGN', p[1], p[3])

# Compound Asignment (+=, -=, *=, /=)
def p_statement_compound_assign(p):
    '''
    compound_assignment_statement : VARIABLE PLUS_EQUAL expression ";"
                                  | VARIABLE MINUS_EQUAL expression ";"
                                  | VARIABLE MUL_EQUAL expression ";"
                                  | VARIABLE DIV_EQUAL expression ";" 
    '''
    p[0] = ('COMPOUND_ASSIGN', p[2], p[1], p[3])

# Print
def p_statement_print(p):
    ''' 
    print_statement : PRINT "(" expression ")" ";"
                    | PRINT expression ";"
    '''
    if len(p) == 4:
        p[0] = ('PRINT', p[2])
    else:
        p[0] = ('PRINT', p[3])

# Echo
def p_statement_echo(p):
    ''' 
    echo_statement : ECHO expression ";"
    '''
    p[0] = ('ECHO', p[2])


# **CONTROL FLOWS**

# If-Else
def p_if_statement(p):
    '''
    if_statement : IF "(" condition ")" block
                 | IF "(" condition ")" block ELSE block
    '''
    if len(p) == 6:
        p[0] = ('IF', p[3], p[5])
    else:
        p[0] = ('IF_ELSE', p[3], p[5], p[7])

# While
def p_statement_while(p):
    '''
    while_statement : WHILE "(" condition ")" block
    '''
    p[0] = ('WHILE', p[3], p[5])

# Block
def p_block(p):
    '''
    block : "{" stmt_list "}"
    '''
    p[0] = p[2]



# **EXPRESSIONS**

# Aritmethic 
def p_expression_binop(p):
    '''
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
               | expression '%' expression
               | expression '.' expression
    '''
    p[0] = ('BINOP', p[2], p[1], p[3])

# Group
def p_expression_group(p):
    '''
    expression : "(" expression ")"
    '''
    p[0] = p[2]

# Number
def p_expression_number(p):
    '''
    expression : LNUMBER
               | DNUMBER
    '''
    p[0] = ('NUM', p[1])

# Variables
def p_expression_var(p):
    '''
    expression : VARIABLE
    '''
    p[0] = ('VAR', p[1])

# Strings
def p_expression_string(p):
    '''
    expression : CONSTANT_ENCAPSED_STRING
    '''
    p[0] = ('STRING', p[1])


# CONDITIONS
def p_condition(p):
    '''
    condition : expression GREATER expression
              | expression LESS expression
              | expression GREATEREQUAL expression
              | expression LESSEQUAL expression
              | expression EQUAL expression
              | expression NOTEQUAL expression
    '''
    p[0] = ('RELOP', p[2], p[1], p[3])


# Error Handling
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")


# Build the Parser
parser = yacc.yacc(debug=True)

def parse(code):
    return parser.parse(code)