import requests
from dateutil import parser as date_parser
from collections import OrderedDict
import matplotlib.dates as plt_dates
import matplotlib.pyplot as plt
import datetime

def get_pings_json():
    r = requests.get('https://poller.moddedminecraft.club/get_pings.php?start_date=2020-01-01=&end_date=2020-04-24')

    return r.json()

def get_dates(server_id, pings_json):
    list = []

    for ping in pings_json:
        if ping['server']['id'] == server_id:
            list.append(datetime.datetime.fromisoformat(ping['pingTime']))
    
    return list

def get_players(server_id, pings_json):
    list = []

    for ping in pings_json:
        if ping['server']['id'] == server_id:
            list.append(ping['players']['online'])

    return list

def get_unique_ids(pings_json):
    l = []

    for ping in pings_json:
        l.append(ping['server']['id'])

    res = list(OrderedDict.fromkeys(l))

    return res

def get_server_names(ids, pings_json):
    dict = {}

    for server_id in ids:
        for ping in pings_json:
            if ping['server']['id'] == server_id:
                dict[server_id] = ping['server']['name']

    return dict

def get_daily_avg(old_dates, old_values):
    total_player_count = 0
    number_of_data_points = 0
    index = 0

    new_dates = []
    new_values = []

    last_start = old_dates[0]
    
    for e in old_dates:
        if e - last_start > datetime.timedelta(hours=1):
            average = total_player_count/number_of_data_points
            new_dates.append(last_start)
            new_values.append(average)

            total_player_count = 0
            number_of_data_points = 0
            last_start += datetime.timedelta(hours=1)
        

        total_player_count += old_values[index]
        number_of_data_points += 1
        index += 1
    
    d = dict()
    d['dates'] = new_dates
    d['values'] = new_values

    return d


json = get_pings_json()
server_ids = get_unique_ids(json)
server_names = get_server_names(server_ids, json)

formatter = plt_dates.DateFormatter('%Y-%m-%d %H:%M:%S')

for server in server_ids:
    dates = get_dates(server, json)
    values = get_players(server, json)

    new = get_daily_avg(dates, values)

    print(new['dates'])
    print('\n')
    print(new['values'])
    
    plt.plot(new['dates'], new['values'], '-o', label=server_names[server])

plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.title('MMCC Playerbase Statistics')
plt.xlabel('Time')
plt.ylabel('Players online')
plt.legend()
plt.grid(linestyle='--', linewidth=0.4)
plt.show()
