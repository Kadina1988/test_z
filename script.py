import csv 
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description='Arguments for script')
parser.add_argument('files', nargs='+', type=str, help='path to files')
parser.add_argument('--report', type=str, help='report')

args = parser.parse_args()

def outline(files, report):
    """Создаем и выводим таблицу в консоль"""
    data_list = parse_data(files)
    calculate_report = prepare_report(data_list, report)
    
    table = tabulate(
        calculate_report,
        headers=['Country', report],
        tablefmt='grid'
    )
    return table


def parse_data(files):
    list_country = []
    for f in files:
        with open(f, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_country.append(row)
    return list_country     


def prepare_report(data, key):
    """Составляет словарь считает сколько строк с каждой страной, и добавляет данные для запрашиваемого отчета """
    countries = {}
    for el in data:
        if el['country'] not in countries:
            countries[el['country']] = {'count': 1, key: float(el[key])}
        else:
            countries[el['country']]['count'] += 1    
            countries[el['country']][key] += float(el[key])    
    
    """Подсчитывает среднее значение для отчета"""
    for k, v in countries.items():
        v[key] = round(v[key] / v['count'], 2)
        del v['count']

    """Сортируем данные по убыванию"""
    sorted_data = sorted([[name, calculate_data[key]] for name, calculate_data in countries.items()], key=lambda x: x[1], reverse=True)
    
    return sorted_data





print(outline(args.files, args.report))
   

