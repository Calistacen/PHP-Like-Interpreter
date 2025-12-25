import streamlit as st
from parser import parse
from interpreter import Interpreter
import sys
import io


# Page Header
st.set_page_config(page_title="PHP-like Interpreter", layout="wide")
st.title("PHP-like Language Interpreter")
st.markdown("Syntax Analyzer and Interpreter Development - Lexer, Parser, Interpreter (PLY)")
st.caption("Project 2 - Compilation Technique LA-09")

# Session state 
if "input" not in st.session_state:
    st.session_state.input = """<?php
$x = 3;
while ($x > 0) {
    print($x);
    $x -= 1;
}
?>"""

if "output" not in st.session_state:
    st.session_state.output = ""


# Syntax Guide
st.sidebar.title("Test Case")

syntax_option = st.sidebar.selectbox(
    "Choose a Test Case:",
    (
        "Simple Statement",
        "Simple Aritmethic Expression",
        "Simple Conditional IF with Block",
        "Simple Looping with Conditional IF Block"
    )
)

# Syntax examples dictionary
syntax_examples = {
    "Simple Statement": """<?php
PRINT "Hello, world!\\n";
ECHO "Welcome ";     
?>""",

    "Simple Aritmethic Expression": """<?php
$num1 = 10;  
$num2 = 20;
$num3 = 30;
$sum = $num1 + $num2 + $num3;
$avg = $sum/3;
PRINT "Num1 is " . $num1 ."\\n";
PRINT "Num2 is " . $num2 ."\\n";
PRINT "Num3 is " . $num3 ."\\n";
PRINT "Sum 3 numbers is " . $sum ."\\n";
PRINT "Average is " . $avg;    
?>""",

    "Simple Conditional IF with Block": """<?php
$num1=10;
$num2=20;
IF ($num1>$num2) {
$bignum = $num1;
PRINT "Big Number is " . $bignum;
}
ELSE {
$bignum = $num2;
PRINT "Big Number is " . $bignum;
}
?>""",

    "Simple Looping with Conditional IF Block": """<?php
PRINT "List of Odd Number 1-100:\\n";
PRINT "\\n";
$num=1;
WHILE ($num<=100) {
IF (($num % 2)!=0) {
$oddnum=$num; 
PRINT "".$num."  "; }
$num=$num+1; }   
?>""",

}

# Display syntax documentation in sidebar
st.sidebar.subheader("Syntax Example")
st.sidebar.code(syntax_examples[syntax_option])

def load_example():
    st.session_state.input = syntax_examples[syntax_option]

st.sidebar.button("Load Example", on_click=load_example)


# Main editor
st.text_area(
    "Write your PHP-like code here:",
    height=300,
    key="input"
)

# Run Button
if st.button("Run Code"):
    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        ast = parse(st.session_state.input)

        if ast is None or ast[0] != 'PROGRAM':
            raise RuntimeError("Invalid program structure")

        interpreter = Interpreter()
        interpreter.run(ast[1])

        st.session_state.output = buffer.getvalue()
        st.success("Program executed successfully!")

    except Exception as e:
        st.session_state.output = f"Error: {e}"

    finally:
        sys.stdout = old_stdout

st.text_area(
    "Output:",
    st.session_state.output,
    height=200
)

# Clear Button
def clear_all():
    st.session_state.input = ""
    st.session_state.output = ""

st.button("Clear", on_click=clear_all)

st.markdown("""
            <style>
            .watermark {
                position: fixed;
                bottom: 10px;
                left: 10px;
                color: white;
                background-color: rgba(0, 0, 0, 0.6); 
                padding: 8px 16px;
                font-size: 13px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                z-index: 9999;
                font-family: 'Segoe UI', sans-serif;
            }
            </style>
            <div class="watermark">
            <div class="watermark-title">Made by Group 6:</div>
            Calista Lianardi – 2702325880<br>
            Carrissa Gloria Herman – 2702322411<br>
            Cathrine Monica Sutanto – 2702319322<br>
            Daniel – 2702321415<br>
            Ririn Saprina Kadang – 2702315715
            </div>
        """, unsafe_allow_html=True)