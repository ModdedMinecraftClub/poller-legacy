import datetime
from database import get_sql_response
from chart_creator import get_avg_chart, get_raw_chart

# ignore this function, it's here just so I was able to test the charts
def write_bytesio_to_file(filename, bytesio):
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())

# get response from the database, give it startDate and endDate:
sql_response = get_sql_response('2019-12-20', '2019-12-24')

# raw chart
# if you want raw chart call this function, returns BytesIO:
b1 = get_raw_chart(sql_response)
# this is just how I used bytesio, you'd obviously serve it via flask as a png:
write_bytesio_to_file('example1.png', b1)

# hourly chart
# create a timedelta => for hourly hours=1, for daily days=1 etc.
delta = datetime.timedelta(hours=1)
# to get the average chart call this function, give it the SQL response and the delta, returns BytesIO:
b2 = get_avg_chart(sql_response, delta)
# this is just how I used bytesio, you'd obviously serve it via flask as a png:
write_bytesio_to_file('example2.png', b2)