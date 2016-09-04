<HTML>
<HEAD>
 <TITLE>Hello World</TITLE>
</HEAD>
<BODY>
<?php
require('api.php');

// Make sure to set proper permission on the file ie 666
$filename = 'wifiPassword.txt';
$daysToExpire = 30;
$routerIp = "192.168.6.1";
$routerUsername = "admin";
$routerPassword = "";



$password = file_get_contents($filename);

if (strlen($password) >= 8 && (time() - filemtime($filename)) <= (60 * 60 * 24 * $daysToExpire))
{
  Print($password);
}
else
{
  $newPassword = str_pad(rand(0, 99999999), 8, '0', STR_PAD_LEFT);
  Print($newPassword);
  $file = fopen($filename, "w") or die("error");
  fwrite($file, $newPassword);
  fclose($file);

  $API = new RouterosAPI();
  $API->debug = false;

  if ($API->connect($routerIp, $routerUsername, $routerPassword))
  {
    $API->comm("/interface/wireless/security-profiles/set", array(".id"=>"Suntree", "wpa-pre-shared-key"=>$newPassword, "wpa2-pre-shared-key"=>$newPassword));
    //$API->write('/interface/wireless/security-profiles/print', false);
    //$API->write("=from=Suntree", true);
    //$READ = $API->read();
    //print_r($READ[0]['wpa2-pre-shared-key']);
    $API->disconnect();
  }

}
?>

</BODY>
</HTML>
