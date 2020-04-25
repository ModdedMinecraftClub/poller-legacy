import datetime
from collections import OrderedDict
from api.database import get_name_by_id


def get_basic_info(sql_response):
    server_ids = get_unique_server_ids(sql_response)
    server_names = get_server_names(server_ids)

    return {"ids": server_ids, "names": server_names}


def get_avg(old_dates_values_dict: dict, timedelta: datetime.timedelta):
    total_player_count = 0
    number_of_data_points = 0
    index = 0

    old_dates = old_dates_values_dict["dates"]
    old_values = old_dates_values_dict["values"]
    new_dates = []
    new_values = []

    last_start = old_dates[0]

    for e in old_dates:
        if e - last_start > timedelta:
            average = total_player_count / number_of_data_points
            new_dates.append(last_start)
            new_values.append(average)

            total_player_count = 0
            number_of_data_points = 0
            last_start += timedelta

        total_player_count += old_values[index]
        number_of_data_points += 1
        index += 1

    return {"dates": new_dates, "values": new_values}


def get_unique_server_ids(sql_response):
    l = []

    for ping in sql_response:
        l.append(ping.serverId)

    r = list(OrderedDict.fromkeys(l))

    return r


def get_server_names(ids):
    d = {}

    for server_id in ids:
        d[server_id] = get_name_by_id(server_id)

    return d


def get_chart_data_by_id(id, sql_response):
    dates_list = []
    values_list = []

    for ping in sql_response:
        if ping.serverId == id:
            dates_list.append(ping.pingTime)
            values_list.append(ping.playersOnline)

    return {"dates": dates_list, "values": values_list}
