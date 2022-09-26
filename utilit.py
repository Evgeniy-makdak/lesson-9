import json
import re


#   загрузка файла со списком студентов из .json
def load_students():
    with open('students.json', 'r', encoding='utf-8') as file:
        return json.load(file)

#   загрузка файла со списком профессий из .json
def load_professions():
    with open('professions.json', 'r', encoding='utf-8') as file:
        return json.load(file)

#   Сравнение введённых данных по id студента с существующим. Если номера такого нет, то возвращаем пустой список.
#   Если такой студент есть, то возвращаем информацию о нём в видет словаря.
def get_student_by_pk(pk):
    student_list = load_students()
    for student in student_list:
        if student['pk'] == pk:
            return student
    return dict()



#print(get_student_by_pk(2))

"""Получаем профессиональные навыки. Возвращается словарь с навыками."""

def get_profession_by_title(title):
    student_profession = load_professions()
    for profession in student_profession:
        if profession['title'] == title:
            return profession


#   print(get_profession_by_title("Testing"))

"""Получаем студента и профессию. Возвращаем что умеет студент, чего не умеет студент и его профпригодность в %."""
def check_fitness(student: dict, profession: dict):
    has_student = list(set(student['skills']).intersection(set(profession['skills'])))

    lacks_student = list(set(profession['skills']).difference(set(student['skills'])))
    fit_percent_student = round((len(has_student) / len(profession['skills']) * 100))
    if len(has_student) == 0:
        has_student = ['0', 'навыков']
    return {
        "has": has_student,
        "lacks": lacks_student,
        "fit_percent": fit_percent_student
    }
#   print(check_fitness(get_student_by_pk(1), get_profession_by_title("Backend")))

"""С помощью регулярного выражения проверяем корректность логина студента"""


def is_correct_login(student_login: str):
    pattern = r'^([^A-Z])(?=.*\d)(?=.*[^@$!%*?&_\-\\.:;])(?=.+[a-zA-Z\d]$).{4,}'

    if re.search(pattern, student_login):
        return True
    else:
        return False


