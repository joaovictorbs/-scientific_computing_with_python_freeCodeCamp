def add_time(start, duration, day=''):
    if len(start) < 4 or len(duration) < 4:
        print('Please, inform a correct value in time clock!')
        quit()

    list_start = list()
    list_duration = list()
    list_start.append(start)
    list_duration.append(duration)
    count = 0
    convert_time = {0: 12, 1: 13, 2: 14, 3: 15, 4: 16, 5: 17, 6: 18, 7: 19, 8: 20, 9: 21, 10: 22, 11: 23}
    days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

    # list start hours
    for i in list_start:
        split_start = i.split()
        time_start = split_start[0].split(':')
        am_pm = i.split()[1]

    # list duration hours
    for i in list_duration:
        time_duration = i.split(':')

    # identifies 60 minutes
    if int(time_start[1]) not in range(0, 60) or int(time_duration[1]) not in range(0, 60):
        print('Inform a range of 59 minutes!')
        quit()

    # check if day exists
    if day != '' and day.capitalize() not in days:
        print('Inform a correct day of the week')
        quit()

        # identifies AM & PM
    if am_pm.upper() == 'PM':
        hour_start = int(time_start[0]) + 12
    elif len(time_start[0]) < 2:
        hour_start = str(0) + time_start[0]
    else:
        hour_start = time_start[0]

    # format duration in 24 hours
    if len(time_duration[0]) < 2:
        hour_duration = str(0) + time_duration[0]
    else:
        hour_duration = time_duration[0]

        # get the minutes
    minutes_start_decimal = int(time_start[1])
    minutes_duration_decimal = int(time_duration[1])

    # format to 24 hours all
    formated_start = str(hour_start) + '.' + str(minutes_start_decimal)
    formated_duration = str(hour_duration) + '.' + str(minutes_duration_decimal)

    # hour total & total days
    total_hour = float(formated_duration) + float(formated_start)

    if int(total_hour / 24) > 0:
        total_days_count = round(total_hour / 24)
    else:
        total_days_count = 0

    if total_days_count < 2 and total_days_count >= 1:
        days_count = ('(next day)')
    elif total_days_count > 1:
        days_count = f'({int(total_days_count)} days later)'
    else:
        days_count = ''

    # identifies future day of the week
    if day != '':
        day = days[day.capitalize()]
        week = list(days.values())
        total_days_count = int(day + total_days_count)

        for i in range(day, total_days_count):
            if count == 7: count = 0
            count += 1
            week.append(count)

        if week[day:total_days_count] != []:
            day = list(week[day:total_days_count])[-1]
            day = list(days.keys())[list(days.values()).index(day)]
        else:
            day = list(days.keys())[list(days.values()).index(day)]

        day = f', {day}'

    # calculate hours and minutes
    hours = int(hour_start) + int(hour_duration)
    minutes = minutes_start_decimal + minutes_duration_decimal
    calculation = hours - (int(hours / 24)) * 24
    final_hour = calculation

    if minutes > 59:
        final_hour += 1
        minutes -= 60

    if len(str(minutes)) < 2: minutes = f'{minutes:02d}'

    if final_hour == 24: final_hour = 0

    if final_hour in convert_time:
        am_pm = 'AM'
    else:
        am_pm = 'PM'

    for k, v in convert_time.items():
        if v == final_hour and v != 12:
            final_hour = k
        elif k == final_hour and k in (0, 24):
            final_hour = v

    # ===========================================FINAL HOUR===========================================
    time = f'{str(final_hour)}:{str(minutes)}'
    # ======================================================================================

    new_time = f'{time} {am_pm}{day} {days_count}'.strip()

    return new_time
