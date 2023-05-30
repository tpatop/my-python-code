from datetime import date
import calendar


# третий четверг месяца
def tcm(year: int):
    for month in range(1, 13):
        month_cal = calendar.monthcalendar(year, month)
        if month_cal[0][3] == 0:
            result = date(year, month, month_cal[3][3])
        else:
            result = date(year, month, month_cal[2][3])
        print(result.strftime('%d.%m.%Y'))


tcm(int(input()))