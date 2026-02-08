import csv 
import argparse
from tabulate import tabulate



def outline(files, report):
    """Создаем и выводим таблицу в консоль"""
    data_list = parse_csv(files)
    calculate_report = prepare_report(data_list, report)
    
    table = tabulate(
        calculate_report,
        headers=['Country', report],
        tablefmt='grid'
    )
    return table


def parse_csv(files:list):
    """
    Парсит csv файлы 
    аргументы передаются в списке при вызове с использованием argparse
    возврацает список
    При получении в аргументах несуществующего файла выдает исключение
    """
    data = []
    for f in files:
        with open(f, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data     


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for script')
    parser.add_argument('files', nargs='+', type=str, help='path to files')
    parser.add_argument('--report', type=str, help='report')
    args = parser.parse_args()
    
    print(outline(args.files, args.report))

   