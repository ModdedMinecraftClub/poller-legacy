import datetime
import io

import api.chart_core as core
import matplotlib.dates as plt_dates
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def get_avg_chart(sql_response, timedelta: datetime.timedelta):
    info = core.get_basic_info(sql_response)

    server_ids = info["ids"]
    server_names = info["names"]

    fig = Figure(figsize=(22, 11))
    ax = fig.add_subplot(1, 1, 1)

    for server in server_ids:
        old_data = core.get_chart_data_by_id(server, sql_response)
        new_data = core.get_avg(old_data, timedelta)

        ax.plot(
            new_data["dates"],
            new_data["values"],
            "-o",
            label=server_names[server],
            markersize=0,
        )

    set_style(ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return output


def get_raw_chart(sql_response):
    info = core.get_basic_info(sql_response)

    server_ids = info["ids"]
    server_names = info["names"]

    fig = Figure(figsize=(22, 11))
    ax = fig.add_subplot(1, 1, 1)

    for server in server_ids:
        data = core.get_chart_data_by_id(server, sql_response)

        ax.plot(data["dates"], data["values"], "-o", label=server_names[server])

    set_style(ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return output


def set_style(ax):
    formatter = plt_dates.DateFormatter("%Y-%m-%d %H:%M:%S")

    ax.xaxis.set_major_formatter(formatter)
    ax.set_title("MMCC Playerbase Statistics")
    ax.set_xlabel("Time")
    ax.set_ylabel("Players online")
    ax.legend()
    ax.grid(linestyle="--", linewidth=0.4)
