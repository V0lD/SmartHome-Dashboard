<?php
// Insert the following 2 lines to /etc/rc.local before exit 0
// service mysql start > /dev/null 2>&1
// php /var/www/html/insertValues.php > /dev/null 2>&1 &



include("yocto_api.php");
include("yocto_temperature.php");
include("yocto_humidity.php");

$servername = "localhost";
$username = "heartnet";
$password = "blackcat";
$dbname = "SmartHome";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error)
{
  die("Connection failed; " . $conn->connect_error);
}

yRegisterHub('http://127.0.0.1:4444');

// Use explicit error handling rather than exceptions
yDisableExceptions();

// Setup the API to use the VirtualHub on local machine
if(yRegisterHub('http://127.0.0.1:4444/',$errmsg) != YAPI_SUCCESS) {
    die("Cannot contact VirtualHub on 127.0.0.1");
}

$serial = yFirstTemperature()->module()->get_serialnumber();
while(TRUE) {
    $temp = yFirstTemperature()->get_currentValue();
    $hum  = yFirstHumidity()->get_currentValue();

    Print("Temperature: $temp C\n");
    Print("Humidity:    $hum %RH\n");
    Print("Serial:      $serial\n");

    if (-40 <= $temp && $temp <= 125 && 0 <= $hum && $hum <= 100)
    {
      $conn->query("insert into YoctoMeteo (YM_Temperature, YM_Humidity, YM_Serial) values ('$temp', '$hum', '$serial')");
    }

    //$sql = "insert into YoctoMeteo (YM_Temperature, YM_Humidity, YM_Serial) values ('$temp', '$hum', '$serial')";
    //if ($conn->query($sql) === FALSE)
    //{
    //  Print("Error: " . $conn->error);
    //}

    sleep(20);
}
?>
