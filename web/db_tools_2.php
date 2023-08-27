<?php
 $host = "localhost";
 $user = "root";
 $password = "";
 function create_connection(){
    $link = mysqli_connect($GLOBALS['host'], $GLOBALS['user'], $GLOBALS['password']) or die("無法建立連接". mysqli_connect_errno()." ".mysqli_connect_error());
    mysqli_query($link, "SET NAMES UTF8");
    return $link;
 }
?> 
