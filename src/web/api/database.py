from pony.orm import Database, db_session

from .config import get_config


@db_session
def get_sql_response(start_date, end_date):
    data = db.select(
        "SELECT pings.serverId,pings.pingTime,pings.playersOnline FROM pings WHERE pings.pingTime <= $end_date AND pings.pingTime >= $start_date ORDER BY pings.pingTime ASC"
    )

    return data

@db_session
def get_name_by_id(server_id):
    data = db.select(
        "SELECT server.serverName FROM server WHERE serverId = $server_id"
    )

    return data[0]

@db_session
def get_all_servers():
    data = db.select(
        "SELECT server.serverId, server.serverName FROM server"
    )

    return data[0]

config = get_config()
db = Database()
db.bind(
    provider="mysql",
    host=config["host"],
    user=config["user"],
    passwd=config["password"],
    db=config["database_name"],
)
