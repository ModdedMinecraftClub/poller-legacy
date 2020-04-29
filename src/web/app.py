import gc

from base64 import b64encode
from datetime import timedelta

from flask import Flask, render_template, request

from api.chart_creator import get_avg_chart, get_raw_chart
from api.database import get_sql_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return render()


@app.route("/", methods=["POST"])
def post():
    f = request.form
    sql_response = get_sql_response(f["from"], f["to"])

    try:
        if not sql_response:
            raise ValueError
        img = get_img(sql_response, f["mode"])
    except ValueError:
        return render(error="No data found for this range or display mode.\nTry a different display mode and if that doesn't work, a different range.", last=f)

    if not img:
        return render(error="Failed to generate chart.", last=f)

    img = b64encode(img.getbuffer()).decode("utf-8")

    gc.collect()
    
    return render(img=img, last=f)


def render(img=None, last={}, error=None):
    return render_template("main.html", img=img, error=error, last=last)


def get_img(sql, mode):
    if mode == "raw":
        return get_raw_chart(sql)

    modes = {
        "week": timedelta(weeks=1),
        "day": timedelta(days=1),
        "hour": timedelta(hours=1),
    }

    return get_avg_chart(sql, modes[mode])
