#This function does not include months as they are not consistent in their number of days
def lts_td(seconds):
    sign_string = '-' if seconds < 0 else ''
    elapsed = abs(int(seconds))
    mns = 60
    hrs = mns * 60
    dys = hrs * 24
    wks = dys * 7
    yrs = dys * 365
    years, remainder = divmod(elapsed, yrs)
    weeks, remainder = divmod(remainder, wks)
    days, remainder = divmod(remainder, dys)
    hours, remainder = divmod(remainder, hrs)
    minutes, remainder = divmod(remainder, mns)
    seconds = remainder
    if years > 0:
       return '%s%dy %dw %dd %dh %dm %ds' % (sign_string, years, weeks, days, hours, minutes, seconds)
    elif weeks > 0:
       return '%s%dw %dd %dh %dm %ds' % (sign_string, weeks, days, hours, minutes, seconds)
    elif days > 0:
        return '%s%dd %dh %dm %ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s%dh %dm %ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s%dm %ds' % (sign_string, minutes, seconds)
    else:
        return '%s%ds' % (sign_string, seconds)
