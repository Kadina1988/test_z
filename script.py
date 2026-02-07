import csv 
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description='Arguments for script')
parser.add_argument('files', nargs='+', type=str, help='path to files')
parser.add_argument('--report', type=str, help='report')

args = parser.parse_args()


def data_analysis(files ,report):
    list_country = []
    for f in files:
        with open(f, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_country.append(row)

    countries = {}

    for el in list_country:
        if el['country'] not in countries:
            countries[el['country']] = {'count': 1, report: float(el[report])}
        else:
            countries[el['country']]['count'] += 1    
            countries[el['country']][report] += float(el[report])    

    for k, v in countries.items():
        v['gdp'] = round(v[report] / v['count'], 2)
        del v['count']
    
    sort_list = sorted([[name, data[report]] for name, data in countries.items()], key=lambda x: x[1], reverse=True)

    table = tabulate(
        sort_list,
        headers=['Country', report],
        tablefmt='grid'
    )

    print(table)


data_analysis(args.files, args.report)    
# print(args.files)
