<?php
  ob_start();
  require('config.php');
  header('Content-Type: application/json');
  echo "[\n";
  foreach($db->query("SELECT serverId,serverName FROM server") as $server){
    $server_name = $server['serverName'];
    $server_id = $server['serverId'];
    echo "\t{\"name\": \"$server_name\", \"id\": $server_id},\n";
  }
  $buffer = ob_get_clean();
  $buffer2 = substr($buffer, 0, strlen($buffer)-2);
  echo $buffer2;
  echo "\n";
  echo "]";
?>
