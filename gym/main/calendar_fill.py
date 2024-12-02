from calendar import monthrange
from datetime import datetime


def fill_cal(year=datetime.now().year, month= datetime.now().month):
    list_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    list_month_index = [1,2,3,4,5,6,7,8,9,10,11,12]
    mont_result = []
    for i in range(len(list_month_index)):
        mont_result.append({'month_index': list_month_index[i], 'month_name': list_month[i]})
    result_list = []
    year_list = []
    for i in range(5):
        year_list.append(datetime.now().year-2+i)
    day_quant = monthrange(year, month)
    for i in range(day_quant[1]):
        date_str = f'{year}-{month}-{i+1}'
        result_list.append({'date': datetime.strptime(f'{date_str} 00:00:00', '%Y-%m-%d %H:%M:%S').date()})
    return  {'date_list': result_list, 'month_list': mont_result, 'year_list': year_list, 'current_year': year, 'current_month': month}




