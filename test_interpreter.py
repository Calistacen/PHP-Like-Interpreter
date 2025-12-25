from parser import parse
from interpreter import Interpreter

code = """
<?php
$num1 = 10;  
$num2 = 20;
$num3 = 30;
$sum = $num1 + $num2 + $num3;
$avg = $sum/3;
PRINT "Num1 is " . $num1 ."\n";
PRINT "Num2 is " . $num2 ."\n";
PRINT "Num3 is " . $num3 ."\n";
PRINT "Sum 3 numbers is " . $sum ."\n";
PRINT "Average is " . $avg;
?> 
"""

ast = parse(code)

print("=== AST ===")
print(ast)

print("\n=== OUTPUT ===")
interp = Interpreter()
interp.run(ast[1])   # ast = ('PROGRAM', stmt_list)
