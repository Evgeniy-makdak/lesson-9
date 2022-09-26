from utilit import *


def main():
    user_input_1 = input(f"Введите id студента.\nПользователь: ")
    dict_student = get_student_by_pk(int(user_input_1))
    student_login = dict_student['login']
    if not dict_student:
        print("У нас нет такого студента")

    else:
        print(is_correct_login(student_login))

        student_skills = ', '.join(dict_student['skills'])
        print(f"Студент {dict_student['full_name']}")
        print(f"Знает {student_skills}")

    user_input_2 = input(f"Выберите специальность для оценки студента Jane Snake.\nПользователь: ")
    dict_profession = get_profession_by_title(user_input_2)
    if not dict_profession:
        print("У нас нет такой специальности")
    else:
        has_student = check_fitness(dict_student, dict_profession)['has']
        lacks_student = check_fitness(dict_student, dict_profession)['lacks']
        fit_percent = check_fitness(dict_student, dict_profession)['fit_percent']
        print("Пригодность", fit_percent, "%")
        print(dict_student['full_name'], 'знает', *has_student)
        print(dict_student['full_name'], 'не знает', *lacks_student)


main()