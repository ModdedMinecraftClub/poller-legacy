import io
import datetime
import chart_core as core
import matplotlib.pyplot as plt

def get_avg_chart(sql_response, timedelta: datetime.timedelta):
    info = core.get_basic_info(sql_response)

    server_ids = info['ids']
    server_names = info['names']
    formatter = info['formatter']

    for server in server_ids:
        old_data = core.get_chart_data_by_id(server, sql_response)
        new_data = core.get_avg(old_data, timedelta)
        
        dates = new_data['dates']
        values = new_data['values']

        plt.plot(dates, values, '-o', label=server_names[server], markersize=0)
    
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    plt.title('MMCC Playerbase Statistics')
    plt.xlabel('Time')
    plt.ylabel('Players online')
    plt.legend()
    plt.grid(linestyle='--', linewidth=0.4)
    
    output = io.BytesIO()
    plt.savefig(output)
    plt.clf()

    return output

def get_raw_chart(sql_response):
    info = core.get_basic_info(sql_response)

    server_ids = info['ids']
    server_names = info['names']
    formatter = info['formatter']

    for server in server_ids:
        data = core.get_chart_data_by_id(server, sql_response)

        dates = data['dates']
        values = data['values']

        plt.plot(dates, values, '-o', label=server_names[server])
    
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    plt.title('MMCC Playerbase Statistics')
    plt.xlabel('Time')
    plt.ylabel('Players online')
    plt.legend()
    plt.grid(linestyle='--', linewidth=0.4)
    
    output = io.BytesIO()
    plt.savefig(output)
    plt.clf()

    return output