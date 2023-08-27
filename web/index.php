<?php

// 連線 server
  require_once("db_tools_2.php");
  $link = create_connection();

// 指定 DB
  $db_name = "log_data";
  mysqli_select_db($link, $db_name) or die ("無法開啟資料庫: ".mysqli_error($link));

// SQL語法 CRUD
  $table = "user_log";
  $sql = "SELECT * FROM {$table}";

// 送出 SQL 並接收搜尋結果
  $results = mysqli_query($link, $sql);

// 擷取紀錄
// seek 指標歸零
// mysqli_data_seek($results, 0);


echo"<!DOCTYPE html><html lang=\"zh-TW\">
<head>
  <title>Ken's resume</title>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <link rel=\"stylesheet\" href=\"bootstrap.min.css\">
  <script src=\"jquery.slim.min.js\"></script>
  <script src=\"popper.min.js\"></script>
  <script src=\"bootstrap.bundle.min.js\"></script>
</head>
<body>
<div class=\"container\">";


// 列出歸零後的 table
  echo "<table class=\"table table-striped table-hover table-borderless table-dark\">";
  while($row = mysqli_fetch_row($results)){
    echo"<tr>";
    for($i = 0; $i < mysqli_num_fields($results); $i++){
      echo "<td>";
      echo "$row[$i]";
      echo "</td>";
    }
    echo "</tr>";    
  }

// 通道關閉
  mysqli_close($link);



  echo"
    </div>
  </body>
  </html>
  ";

?> 
