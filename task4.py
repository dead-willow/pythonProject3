import csv

def middle_salary(salary_sum, vacancy_num):
    """Функция для вычсления средней зарплаты

    Описание аругментов:
    salary_sum - сумма всех заплат
    vacancy_num - количество вакансий

    """
    return salary_sum/vacancy_num
def pr_sootnoshenie(sr_salary, average_salary):
    """Функция для вычсления отношения средней зарплаты к любой другой

        Описание аругментов:
        sr_salary - средняя зарплата
        average_salary - сравниваемая вакансия

        """
    m = average_salary/sr_salary*100
    return m[:3]

data = {}
numb = {}
a = {}
keys = []
comparison = []
with open ('D:\\docs\\Student-627\\Downloads\\vacancy.csv', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"')
    for el in reader:
        keys.append([el['Work_Type']])
        data[el['Work_Type']] = data.get(el['Work_Type'], 0) + int(el['\ufeffSalary'])
        numb[el['Work_Type']] = data.get(el['Work_Type'], 0) + 1
    for Salary, Work_Type, Company_Size, Role, Company in reader:
        m = middle_salary(int(data[Work_Type]), int(numb[Work_Type]))
        a[el['Work_Type']] = data.get(el['Work_Type'], 0) + m
    for row in reader:
        row['percent'] = pr_sootnoshenie(int(Salary), a[row['Work_Type']])
        comparison.append(row)
with open ('D:\\docs\\Student-627\\Downloads\\vacancy_procent.csv','w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, fieldnames=['Salary', 'Work_Type', 'Company_Size', 'Role', 'Company', 'procent'])
    w.writeheader()
    w.writerows(comparison)