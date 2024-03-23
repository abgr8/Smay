<?php
$imgL = "1";
$imgR = "1";
$selectedimg = null;
function selectimgs($selectedimg) {
    $GLOBALS['imgL'] = $selectedimg;
    do {
        $GLOBALS['imgR'] = random_int(1, 17);
    } while ($GLOBALS['imgL'] === $GLOBALS['imgR']);
}
if (is_null($selectedimg)){
selectimgs(random_int(1,17));}

?>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Choose Your Image</title>
  <link rel="stylesheet" href="style.css">
</head>
<body class="dark-theme">
<header>
  <h1>$may</h1>
</header>
<main>
  <div class="image-container">
    <button>  <img src="<?php echo"/ppl/".$imgL.".jpeg";?>" alt="Image 1" class="image-choice"> </button>
    <button>  <img src="<?php echo"/ppl/".$imgR.".jpeg" ?>" alt="Image 2" class="image-choice"> </button>
  </div>
</main>
</body>
</html>
<!--written by the smay teammm!!!-->