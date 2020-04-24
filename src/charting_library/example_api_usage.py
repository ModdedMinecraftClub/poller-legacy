import datetime
from database import get_sql_response
from chart_creator import get_avg_chart, get_raw_chart

def write_bytesio_to_file(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does
    not exist yet. 
    """
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())

sql_response = get_sql_response("2019-12-20", "2019-12-24")

# raw chart
b1 = get_raw_chart(sql_response)
write_bytesio_to_file('example1.png', b1)

# hourly chart
delta = datetime.timedelta(hours=1)
b2 = get_avg_chart(sql_response, delta)
write_bytesio_to_file('example2.png', b2)