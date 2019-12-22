<?php
  ob_start();
  require('config.php');

  if(!isset($_GET['start_date']) || !isset($_GET['end_date'])){
    echo 'You must specify start_date and end_date via GET parameters.';
    exit;
  }

  header('Content-Type: application/json');

  echo "[\n";
  $statement = $db->prepare('SELECT pings.serverId,pings.pingTime,pings.playersOnline,pings.playersMax,server.serverName FROM pings INNER JOIN server ON server.serverId=pings.serverId WHERE pings.pingTime<=:end AND pings.pingTime>=:start');
  $statement->bindParam('end', $_GET['end_date']);
  $statement->bindParam('start', $_GET['start_date']);
  $statement->execute();
  $found_something = false;
  while($row = $statement->fetch()){
    $found_something = true;
    $ping_time = $row['pingTime'];
    $server_name = $row['serverName'];
    $server_id = $row['serverId'];
    $online_players = $row['playersOnline'];
    $max_players = $row['playersMax'];
    echo "    {
      \"pingTime\": \"$ping_time\",
      \"server\": {
        \"name\": \"$server_name\",
        \"id\": $server_id
      },
      \"players\": {
        \"online\": $online_players,
        \"max\": $max_players
      }
    },\n";
  }
  if($found_something){
    $buffer = ob_get_clean();
    $buffer2 = substr($buffer, 0, strlen($buffer)-2);
    echo $buffer2;
  }
  echo "\n";
  echo "]";
?>
