<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>HTML Graphs</title>

<style>

      img { padding-left: 35%; padding-top: 5%;}
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
</head>

<body>
  <nav>
  <ul class="top-menu">
    <li class="top"><a href="../web/index.php">Home</a><div class="menu-item" id="home"></div></li>
    <li class="top"><a href="../barchart/index.php">Barchart</a><div class="menu-item" id="cataloge"></div></li>
    <li class="top"><a href="../piechart/index.php">Piechart</a><div class="menu-item" id="cataloge"></div></li>
    <li class="top"><a href="index.php">Sentiment</a><div class="menu-item" id="cataloge"></div></li>

  </ul>
</nav>
<?php
$myfile = fopen("../../values.txt","r");
$values =  fread($myfile,10);
fclose($myfile);
$pos = $values[0];
$pos = 100*((float)$pos)/7;
$neg = 100 - $pos;
$confidence = $values[2].$values[3].$values[4].$values[5].$values[6].$values[7];
echo "Confidence".$confidence;
if($pos > 50)
	echo '<img src="happy.jpg">';
else
	echo '<img src="sad.png">';
?>


  <!-- <h2>Bubble Chart</h2>
  <div class="chart">
    <div data-value="7" data-label="500" data-x="50" data-y="50" class="chart-bubble"></div>
    <div data-value="10" data-label="1000"  data-x="10" data-y="60" class="chart-bubble"></div>

    <div class="lines">
      <div class="lines-horz"></div>
      <div class="lines-horz"></div>
      <div class="lines-horz"></div>
      <div class="lines-horz"></div>
      <div class="lines-vert"></div>
      <div class="lines-vert"></div>
      <div class="lines-vert"></div>
      <div class="lines-vert"></div>
    </div>
  </div> -->

</body>
</html>
