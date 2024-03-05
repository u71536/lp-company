"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]

    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]
print('Названия отделов')
for department in departments:
    print(department['title'])

print('\nИмена сотрудников ')
for i in departments:
    for k in i['employers']:
        print(k['first_name'])

print('\nИмена сотрудников с названием отдела')
for i in departments:
    for k in i['employers']:
        print(f"{k['first_name']} работает в {i['title']}")

print('\nИмена сотрудников с названием отдела >100К')
for i in departments:
    for k in i['employers']:
        if k['salary_rub'] >= 100000:
            print(f"{k['first_name']} работает в {i['title']}")

print('\nВывести позиции с зп <80К')
for i in departments:
    for k in i['employers']:
        if k['salary_rub'] <= 80000:
            print(f"{k['position']}")

print('\nВывести траты на каждый отдел')
d = []
for i in departments:
    for k in i['employers']:
        d.append(k['salary_rub'])
    print(f'{i["title"]} тратит {sum(d)}')


print('\nВывести отдел и минимальную зарплату')
d = []
for i in departments:
    for k in i['employers']:
        d.append(k['salary_rub'])
    print(f'В {i["title"]} наименьшая зарплата {min(d)}')
    d.clear()

print('\nВывести отдел и минимальную, средную и максимальную зарплаты')
d = []
for i in departments:
    for k in i['employers']:
        d.append(k['salary_rub'])
    avg_salary = sum(d) / len(d)
    print(f'В {i["title"]} наименьшая зарплата {min(d)}, средняя {int(avg_salary)}, наибольшая зарплата {max(d)}')
    d.clear()

print('\nВывести средную зарплату в компании')
d = []
for i in departments:
    for k in i['employers']:
        d.append(k['salary_rub'])
    avg_salary = sum(d) / len(d)
print(f'Средняя зарплата в компании: {int(avg_salary)}')

print('\nВывести позиции с зп >90К без повторений')
for i in departments:
    for k in i['employers']:
        if k['salary_rub'] > 90000:
            print(f"{k['position']}")

print('\nВывести среднюю зарплату по каждому отделу среди девушек')
girls_names = ["Michelle", "Nicole", "Christina", "Caitlin"]
d = []
for i in departments:
    for k in i['employers']:
        if k['first_name'] in girls_names:
            d.append(k['salary_rub'])
        else:
            continue
    avg_salary = sum(d) / len(d)
    print(f"Средняя зарплата в компании по отделам среди девушек. {i['title']} {int(avg_salary)}")
    d.clear()

print('\nВывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву')
letters = ["a", "e", "u", "i", 'o', 'y']
for i in departments:
    for k in i['employers']:
        p = k['last_name'].split()
        if p[0][-1] in letters:
            print(f"{k['first_name']}")
        else:
            continue


"""Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""