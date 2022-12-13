def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Вывести список всех сотрудников")
    print("10. Прочитать данные в формате json и вывести на экран")
    print("11. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
    #Добавлены пункты 9 и 10


def show_search_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Найти сотрудника по идентификатору")
    print("2.  Найти сотрудника по фамилии")
    print("3.  Найти сотрудника по телефонному номеру")
    return int(input("Введите номер необходимого действия: "))


def show_update_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Обновить данные сотрудника по идентификатору")
    print("2.  Обновить данные сотрудника по фамилии")
    return int(input("Введите номер необходимого действия: "))


def get_id() -> int:
    return int(input("Введите идентификатор сотрудника: "))


def get_last_name() -> str:
    return input("Введите фамилию сотрудника: ")


def get_first_name() -> str:
    return input("Введите имя сотрудника: ")


def get_position() -> str:
    return input("Введите должность сотрудника: ")


def get_phone_number() -> str:
    return input("Введите телефон сотрудника: ")


def get_salary() -> float:
    return float(input("Введите зарплату сотрудника: "))


def get_salary_range() -> tuple:
    lo = float(input("Введите начало диапазона занчений: "))
    hi = float(input("Введите конец диапазона занчений: "))
    return lo, hi


def get_employee() -> dict:
    result = {}
    result["id"] = get_id()
    result["last_name"] = get_last_name()
    result["first_name"] = get_first_name()
    result["position"] = get_position()
    result["phone_number"] = get_phone_number()
    result["salary"] = get_salary()
    return result


def get_changes() -> int:
    print("\nВыберите данные, которые необходимо изменить:")
    print("1. Идентификатор")
    print("2. Фамилия")
    print("3. Имя")
    print("4. Должность")
    print("5. Телефон")
    print("6. Заработная плата")
    return int(input("Введите номер выбранного пункта: "))


def no_employee_error():
    print("Такого сотрудника нет в базе")


def show_employee_info(employee: dict):
    for k, v in employee.items():
        print(f'{k}: {v}')

#Добавлена функция вывода всего списка на экран
def show_employee(employees: dict):
    if len(employees) > 0:
        print("ИД".center(20), "Фамилия".center(20), "Имя".center(20), "Должность".center(20), "Телефон".center(20), "Зар.плата".center(20))
        print("-"*130)
        for item in employees:
            print(' '.join([str(v).center(20) for v in item.values()]))
    else:
        print("Список пуст!")