



import datetime as dt

#abdul used a function and special comparison
def prev_day(day):
    #day is a day of week all lower case
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    today = dt.date.today()
    t_dw = today.weekday()
    dw = week_days.index(day)  #get the index using the passed string
    diff = dw - t_dw

    if diff < 0:
        new_date = today + dt.timedelta(diff)
    else:
        new_date = today - dt.timedelta(7-diff)

    return new_date


print ('Today : ', dt.date.today())
print ('Prev: ', prev_day('thursday'))

           