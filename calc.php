<?php
$num1 = $_REQUEST ['num1'];
$num2 = $_REQUEST ['num2'];
$op = $_REQUEST ['op'];
$res=0;

if ($op=='add')
{
    $res=$num1+$num2;
}

else if($op=='subtract')
{
    $res=$num1-$num2;
}

else if($op=='multiply')
{
    $res=$num1*$num2;
}

else if($op=='divide')
{
    $res=$num1/$num2;
}
print "Rayona Young <br> Assignment 5: Calc.htm <br><br>";
print <<< Here
Number1: $num1 <br>
Number2: $num2 <br>
Operation: $op <br>
Result: $res <br>
Here;
?>
