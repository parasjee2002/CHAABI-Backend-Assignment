from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference in days
    date_difference = abs((to_date_obj - from_date_obj).days)

    # Compare the difference with the given value
    if date_difference < difference:
        return True
    else:
        return False
x='02-02-06'
y='13-12-11'
print(check_date_difference(x,y,12))
