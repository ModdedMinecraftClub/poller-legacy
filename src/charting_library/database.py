from pony.orm import db_session, Database
from config import get_config

@db_session
def get_sql_response(start_date, end_date):
    data = db.select(
        "SELECT pings.serverId,pings.pingTime,pings.playersOnline,pings.playersMax,server.serverName FROM pings INNER JOIN server ON server.serverId=pings.serverId WHERE pings.pingTime <= $end_date AND pings.pingTime >= $start_date ORDER BY pings.pingTime ASC"
    )

    return data

config = get_config()
db = Database()
db.bind(provider='mysql', host=config['host'], user=config['user'], passwd=config['password'], db=config['database_name'])
