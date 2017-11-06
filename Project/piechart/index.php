<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>JS Pie Chart V2</title>
  <style>
  .top-menu {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #333;
  }

  .top {
      float: left;
  }

  .top a {
      display: block;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
  }

  .top a:hover:not(.active) {
      background-color: #111;
  }

  .active {
      background-color: #4CAF50;
  }
  </style>



      <style>
      /* NOTE: The styles were added inline because Prefixfree needs access to your styles and they must be inlined if they are on local disk! */
      div {
  width: 100%;
  text-align: center;
}
div p {
  text-align: center;
  font-family: "Arial", sans-serif;
  font-size: 16px;
  color: #bdc3c7;
}
    </style>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>

</head>
<?php
$myfile = fopen("../../values.txt","r");
$values =  fread($myfile,10);
fclose($myfile);
$pos = $values[0];
$pos = 100*((float)$pos)/7;
$neg = 100 - $pos;
$confidence = $values[2].$values[3].$values[4].$values[5].$values[6].$values[7];
echo "Confidence".$confidence;
echo    '<script type="text/javascript">
	    var val1 = '.$pos.';
	    var val2 = '.$neg.';
	    var myData = [val2,val1];
    </script>';
?>

<body>
  <nav>
  <ul class="top-menu">
    <li class="top"><a href="../web/index.php">Home</a><div class="menu-item" id="home"></div></li>
    <li class="top"><a href="../barchart/index.php">Barchart</a><div class="menu-item" id="cataloge"></div></li>
    <li class="top"><a href="index.php">Piechart</a><div class="menu-item" id="home"></div></li>
    <li class="top"><a href="../emoji/index.php">Sentiment</a><div class="menu-item" id="cataloge"></div></li>
  </ul>
</nav>
  <div>
  <p>Variations on Greeting the World</p>
  <canvas id="canvas" width="600" height="400">
    No Love for HTML5 eh?
  </canvas>
  <p>Change the 'myData' values to see the labels dynamically adjust.</p>
</div>

    <script  src="js/index.js"></script>

</body>
</html>
