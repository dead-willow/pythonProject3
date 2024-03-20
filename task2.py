import csv

with open ('D:\\docs\\Student-627\\Downloads\\vacancy.csv', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter=';', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while float(reader[j]['Company_Size'])<float(key['Company_Size']) and j>0:
            reader[j+1] = reader[j]
            j-=1
        reader[j] = key
    for el in reader:
        if 'классный руководитель' in el['Role']:
            print(f"В компании {el['Company']} есть заданная профессия: {el['Role']}, з/п в такой компании составит:", el['\ufeffSalary'])
            break