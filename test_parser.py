from parser import parse

code = """
<?php
$x = 5;
print($x);
print 5;
echo ("Hello");
?>
"""

ast = parse(code)

print("=== AST OUTPUT ===")
print(ast)