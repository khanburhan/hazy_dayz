def hazy_dayz():
    days = ["monday", "tuesday", "thursday", "friday", "saturday", "sunday"]

    for d in days:
        if "sunday" in d:
            sunday_index = days.index('sunday')
            tomorrow = days[sunday_index - 1]
            current_day = days[days.index(tomorrow) - 1]
            day_before = days[days.index(current_day) - 1]
            # print(current_day)
            visiting_day = days[days.index(current_day) - days.index(
                day_before) - days.index(day_before) + days.index(tomorrow) + 1]
            print("Visiting Day is", visiting_day.title())


hazy_dayz()
