from datetime import datetime, timedelta

def get_previous_date(date, n):
    # Convert date string to datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the timedelta for n days
    timedelta_obj = timedelta(days=n)

    # Subtract the timedelta from the date_obj to get the previous date
    previous_date_obj = date_obj - timedelta_obj

    # Convert the previous_date_obj back to string format
    previous_date = previous_date_obj.strftime('%y-%m-%d')

    return previous_date
x='16-12-10'
y=11
print(get_previous_date(x,y))