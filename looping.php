<?php
PRINT "List of Odd Number 1-100:\n";
PRINT "\n";
$num=1;
WHILE ($num<=100) {
IF (($num % 2)!=0) {
$oddnum=$num; 
PRINT "".$num."  "; }
$num=$num+1; }   
?>