import calendar
from datetime import date


today = str(date.today())
today_year = int(today[0:4])
today_month = int(today[5:7])
today_day = int(today[8:10])

holidays = []

def date_range(start, end):

    start_year = int(start[0:4])
    start_month = int(start[5:7])
    start_day = int(start[8:10])

    end_year = int(end[0:4])
    end_month = int(end[5:7])
    end_day = int(end[8:10])

    num_of_days_in_month = calendar.monthrange(start_year, start_month)[1]

    for year in range(start_year, end_year+1):

        if start_year == end_year:

            for month in range(start_month, end_month+1):
                num_of_days_in_month = calendar.monthrange(year, month)[1]
                if start_month == end_month:
                    for day in range(start_day, end_day+1):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")
                else:

                    if month == start_month:

                        for day in range(start_day, num_of_days_in_month+1):
                            if month < 10:
                                if day < 10:
                                    holidays.append(f"{year}-0{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-0{month}-{day}")
                            else:
                                if day < 10:
                                    holidays.append(f"{year}-{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-{month}-{day}")

                    elif month == end_month:

                        for day in range(1, end_day+1):
                            if month < 10:
                                if day < 10:
                                    holidays.append(f"{year}-0{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-0{month}-{day}")
                            else:
                                if day < 10:
                                    holidays.append(f"{year}-{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-{month}-{day}")

                    else:
                        
                        for day in range(1, num_of_days_in_month):
                            if month < 10:
                                if day < 10:
                                    holidays.append(f"{year}-0{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-0{month}-{day}")
                            else:
                                if day < 10:
                                    holidays.append(f"{year}-{month}-0{day}")
                                else:
                                    holidays.append(f"{year}-{month}-{day}")

        elif year == start_year:

            for month in range(start_month, 13):
                num_of_days_in_month = calendar.monthrange(year, month)[1]

                if month == start_month:

                    for day in range(start_day, num_of_days_in_month+1):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")

                else:
                        
                    for day in range(1, num_of_days_in_month):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")
        
        elif year == end_year:

            for month in range(1, end_month+1):
                num_of_days_in_month = calendar.monthrange(year, month)[1]

                if month == end_month:

                    for day in range(1, end_day+1):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")

                else:
                        
                    for day in range(1, num_of_days_in_month):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")

        else:

            for month in range(1, 13):
                num_of_days_in_month = calendar.monthrange(year, month)[1]
                if year == end_year and month > end_month:
                    break
                else:

                    for day in range(1, num_of_days_in_month+1):
                        if month < 10:
                            if day < 10:
                                holidays.append(f"{year}-0{month}-0{day}")
                            else:
                                holidays.append(f"{year}-0{month}-{day}")
                        else:
                            if day < 10:
                                holidays.append(f"{year}-{month}-0{day}")
                            else:
                                holidays.append(f"{year}-{month}-{day}")

print("1- Today to <date> without holidays")
print("2- Today to <date> with holidays")
print("3- <date> to <date> without holidays")
print("4- <date> to <date> with holidays")
print("5- Exit")

option = int(input("Choose an option from 1 to 5: "))

while option != 5:

    if option == 1 or option == 2:

        from_year = today_year
        from_month = today_month
        from_day = today_day

    if option == 3 or option == 4:

        from_date = input("Enter the date to count from (yyyy-mm-dd): ")
        from_year = int(from_date[0:4])
        from_month = int(from_date[5:7])
        from_day = int(from_date[8:10])

    to_date = input("Enter the date to count to (yyyy-mm-dd): ")
    to_year = int(to_date[0:4])
    to_month = int(to_date[5:7])
    to_day = int(to_date[8:10])

    if option == 2 or option == 4:

        holiday_start = input("Enter holiday start date (yyyy-mm-dd): ")
        holiday_end = input("Enter holiday end date (yyyy-mm-dd): ") 

        date_range(holiday_start, holiday_end)

    num_of_days_in_month = calendar.monthrange(from_year, from_month)[1]
    count_days = 0

    while from_year < to_year or from_month < to_month or from_day < to_day:

        holiday = False

        for i in holidays:
            if from_year == int(i[0:4]) and from_month == int(i[5:7]) and from_day == int(i[8:10]):
                holiday = True
                break
            
        if calendar.weekday(from_year, from_month, from_day) != 4 and not holiday:
            count_days += 1

        from_day += 1

        if from_day > num_of_days_in_month:

            from_day = 1
            from_month += 1

            if from_month > 12:

                from_month = 1
                from_year += 1
            
        num_of_days_in_month = calendar.monthrange(from_year, from_month)[1]

    print(str(count_days) + " business days")

    print("-----------------------------------------")
    print("1- Today to <date> without holidays")
    print("2- Today to <date> with holidays")
    print("3- <date> to <date> without holidays")
    print("4- <date> to <date> with holidays")
    print("5- Exit")

    option = int(input("Choose an option from 1 to 5: "))