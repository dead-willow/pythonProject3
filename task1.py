import csv

with open ('D:\\docs\\Student-627\\Downloads\\vacancy.csv', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    ans = list(reader)[1:]
    max_salary_size = []
    for salary, typee, size, role, company in ans:
        max_salary_size.append(salary)
    max_salary_size = sorted(max_salary_size)
    salary_size = {}
    for el in ans:
        if max_salary_size[-1]==int(el[1]):
            salary_size[el[-2]] = salary_size.get(el[1], 0)+1

with open ('D:\\docs\\Student-627\\Downloads\\vacancy_new.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.writer(f)
    w.writerow(['company', 'role', 'Salary'])
    for salary, typee, size, role, company in ans:
        w.writerows(ans)
