# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def show_menu() -> int:
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по имени или фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Удалить данные из справочника\n"
        "6. Изменить данные в справочнике\n"
        "7. Сохранить справочник в текстовом формате\n"
        "8. Закончить работу"
    )
    choice = int(input("Введите действие: "))
    return choice


def show_change_menu() -> int:
    print(
        "\nВыберите необходимое действие:\n"
        "1. Изменить фамилию\n"
        "2. Изменить имя\n"
        "3. Изменить номер телефона\n"
        "4. Изменить описание\n"
        "5. Выйти из режима редактирования\n"
    )
    choice = int(input("Введите действие: "))
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data


def write_csv(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as fout:
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ","
            fout.write(f"{s[:-1]}\n")


def print_result(phone_book):
    print("Фамилия", "Имя", "Телефон", "Описание")
    for i in range(len(phone_book)):
        s = f"{i+1}. "
        for v in phone_book[i].values():
            s += v + ", "
        print(s[:-2])


def get_search_name() -> str:
    choice = input("Введите имя или фамилию: ").lower().replace(" ", "")
    return choice


def find_by_name(phone_book, lastName) -> str:
    sout = ""
    for item in phone_book:
        s = ""
        if item["Фамилия"].lower() == lastName or item["Имя"].lower() == lastName:
            for v in item.values():
                s += v + ",".ljust(3)

            sout += s[:-3] + "\n"
    return "Не найдено" if len(sout) == 0 else sout


def get_search_number() -> str:
    num = input("Введите номер: ").lower().replace(" ", "")
    return num


def find_by_number(phone_book, number) -> str:
    sout = ""
    for item in phone_book:
        s = ""
        if item["Телефон"].lower() == number:
            for v in item.values():
                s += v + ",".ljust(3)
            sout += s[:-3] + "\n"
    return "Не найдено" if len(sout) == 0 else sout


def get_new_user():
    lastName = input("Введите фамилию: ").replace(" ", "")
    name = input("Введите имя: ").replace(" ", "")
    number = input("Введите номер: ").replace(" ", "")
    description = input("Введите описание: ")
    user_data = {
        "Фамилия": lastName,
        "Имя": name,
        "Телефон": number,
        "Описание": description,
    }
    return user_data


def add_user(phone_book, user_data):
    phone_book.append(user_data)


def get_file_name():
    file_name = input("Введите имя файла: ").replace(" ", "_") + ".txt"
    return file_name


def write_txt(file_name, phone_book):
    with open(file_name, "w", encoding="utf-8") as fout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            fout.write(f"{s[:-1]}\n")
    print("Готово!")


def get_num_user():
    user_num = int(input("Введите номер записи: "))
    return user_num


def get_lastName():
    lastName = input("Введите фамилию: ").replace(" ", "")
    return lastName


def get_name():
    name = input("Введите имя: ").replace(" ", "")
    return name


def get_number():
    number = input("Введите номер: ").replace(" ", "")
    return number


def get_discription():
    description = input("Введите описание: ")
    return description


def delete_user(phone_book, user_num):
    try:
        phone_book.pop(user_num - 1)
    except Exception:
        print("Такой записи не существует")
    else:
        write_csv("phonebook.csv", phone_book)
        print("Запись удалена успешно")


def change_params(phone_book, user_num, key, val):
    phone_book[user_num - 1][key] = val


def сhange_phonebook(phone_book, user_num):
    choice = show_change_menu()
    while choice != 5:
        if choice == 1:
            lastName = get_lastName()
            change_params(phone_book, user_num, "Фамилия", lastName)
            # phone_book[user_num]["Фамилия"] = lastName
        elif choice == 2:
            name = get_name()
            change_params(phone_book, user_num, "Имя", name)
            # phone_book[user_num]["Имя"] = name
        elif choice == 3:
            number = get_number()
            change_params(phone_book, user_num, "Телефон", number)
            # phone_book[user_num]["Телефон"] = number
        elif choice == 4:
            discription = get_discription()
            change_params(phone_book, user_num, "Описание", discription)
            # phone_book[user_num]["Описание"] = discription
        choice = show_change_menu()
    print("Конец!")


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv("phonebook.csv")

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            lastName = get_search_name()
            print(lastName)
            print(find_by_name(phone_book, lastName))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv("phonebook.csv", phone_book)
        elif choice == 5:  # delte
            print_result(phone_book)
            user_num = get_num_user()
            delete_user(phone_book, user_num)
        elif choice == 6:  # change
            print_result(phone_book)
            user_num = get_num_user()
            сhange_phonebook(phone_book, user_num)
            write_csv("phonebook.csv", phone_book)
        elif choice == 7:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()
    print("Конец!")


work_with_phonebook()
