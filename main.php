
<?php
#$test = '/usr/bin/python2 /var/www/html/software2/test.py';
#echo exec($test);
$command = escapeshellcmd("python /var/www/html/software2/scapper.py");
$output = shell_exec($command);
echo $output;
header('Location: runalgo.php');
#$command = escapeshellcmd("python /var/www/html/software2/algoscript.py");
#$output = shell_exec($command)
#echo $output;
#$test = `python /var/www/html/software2/test.py`; 
#echo $test;
?>
