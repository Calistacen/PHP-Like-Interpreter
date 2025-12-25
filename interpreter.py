class Interpreter:
    def __init__(self):
        self.vars = {}   # symbol table

    # evaluating the AST from parser
    def eval_expr(self, expr):
        etype = expr[0]

        # Number
        if etype == 'NUM':
            return expr[1]

        # Strinng
        elif etype == 'STRING':
            raw = expr[1].strip('"').strip("'")
            # interpret escape sequences like \n
            return raw.encode('utf-8').decode('unicode_escape')

        # Variable
        elif etype == 'VAR':
            varname = expr[1]
            return self.vars.get(varname, 0)

        # Binary Operations
        elif etype == 'BINOP':
            _, op, left, right = expr
            lval = self.eval_expr(left)
            rval = self.eval_expr(right)

            if op == '+': return lval + rval
            if op == '-': return lval - rval
            if op == '*': return lval * rval
            if op == '/': return lval / rval
            if op == '%': return lval % rval
            if op == '.': return str(lval) + str(rval)

    # relational/conditional evaluation
    def eval_condition(self, cond):
        _, op, left, right = cond
        lval = self.eval_expr(left)
        rval = self.eval_expr(right)

        if op == '>': return lval > rval
        if op == '<': return lval < rval
        if op == '>=': return lval >= rval
        if op == '<=': return lval <= rval
        if op == '==': return lval == rval
        if op == '!=': return lval != rval

    # Statement execution
    def exec_stmt(self, stmt):
        stype = stmt[0]
    
        # Assignment 
        if stype == 'ASSIGN':
            _, var, expr = stmt
            self.vars[var] = self.eval_expr(expr)

        # Compound assignment
        elif stype == 'COMPOUND_ASSIGN':
            _, op, var, expr = stmt
            value = self.eval_expr(expr)

            if var not in self.vars:
                raise RuntimeError(f"Undefined variable {var}")

            if op == '+=': self.vars[var] += value
            elif op == '-=': self.vars[var] -= value
            elif op == '*=': self.vars[var] *= value
            elif op == '/=': self.vars[var] /= value
            elif op == '%=': self.vars[var] %= value

        # Print & Echo
        elif stype == 'PRINT':
            print(self.eval_expr(stmt[1]), end='')

        elif stype == 'ECHO':
            print(self.eval_expr(stmt[1]))

        # If/ If-Else
        elif stype == 'IF':
            _, cond, block = stmt
            if self.eval_condition(cond):
                self.run(block)

        elif stype == 'IF_ELSE':
            _, cond, then_block, else_block = stmt
            if self.eval_condition(cond):
                self.run(then_block)
            else:
                self.run(else_block)
        
        # While Loop
        elif stype == 'WHILE':
            _, cond, block = stmt
            while self.eval_condition(cond):
                self.run(block)

    # Program runner
    def run(self, program):
        for stmt in program:
            self.exec_stmt(stmt)


