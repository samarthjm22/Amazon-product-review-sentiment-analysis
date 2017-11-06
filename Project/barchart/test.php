<?php
$myfile = fopen("../../values.txt","r");
echo fread($myfile,10);
fclose($myfile);
?> 

