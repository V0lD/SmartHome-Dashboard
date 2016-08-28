<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>Loop Images</title>
  <script type="text/javascript">
    var index=0;
    function changeBanner(){
      [].forEach.call(document.images,function (v,i) { document.images[i].hidden = i!==index});
      index = (index+1) % document.images.length;
    }
    window.onload = function () {setInterval(changeBanner, 50)};
  </script>
</head>
<body>
  <div style="width:1020px;height:702px;overflow:hidden;">
  
<?php

$files = glob('satelliteImages/*.jpg');
usort($files, function($a, $b) {
  return filemtime($a) > filemtime($b);
});

foreach($files as $file){
  printf('<img src="%1$s" />', $file);
}

?>

  </div>
</body>
</html>
