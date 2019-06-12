
def formatting_elapsed_time(elapse_time):

    days, rest_time = divmod(elapse_time,86400)
    days = str(int(days)).zfill(2)
    hours, rest_time = divmod(rest_time,3600)
    hours = str(int(hours)).zfill(2)
    minutes, rest_time = divmod(rest_time,60)
    minutes = str(int(minutes)).zfill(2)
    seconds_int, seconds_dec = divmod(rest_time,1)
    seconds_int = str(int(seconds_int)).zfill(2)
    seconds_dec = str(int(seconds_dec*10))
    return(days+"d:"+hours+"h:"+minutes+"m:"+seconds_int+"."+seconds_dec+"s")

