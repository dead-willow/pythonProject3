import csv

with open ('D:\\docs\\Student-627\\Downloads\\vacancy.csv', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"')
    data = sorted(reader, key=lambda x: x['Company'])

    name = input('Введите название компании:')

    while name != 'None':
        for i in data:
            if name == i['Company']:
                print(f"В {i['Company']} найдена вакансия: {i['Role']}. З/п составит:", i['\ufeffSalary'])
                break
        else:
            print('К сожалению, ничего не удалось найти')
        name = input('Введите название компании:')


