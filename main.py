user_data = []

while True:
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Вывести информацию о пользователях")
    print("4. Вычислить средний возраст")
    print("5. Выйти")

    choice = input("Выберите действие (1/2/3/4/5): ")

    if choice == '1':
        name = input("Введите имя пользователя: ")
        age = input("Введите возраст пользователя: ")
        try:
            age = int(age)
        except ValueError:
            print("Ошибка: неверный формат возраста")
            continue

        user_data.append({'name': name, 'age': age})

    elif choice == '2':
        name = input("Введите имя пользователя для удаления: ")
        for user in user_data:
            if user['name'] == name:
                user_data.remove(user)
                print(f"Пользователь {name} удален")
                break
        else:
            print(f"Пользователь {name} не найден")

    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")

    elif choice == '4':
        if len(user_data) == 0:
            print("Нет данных о пользователях")
        else:
            total_age = 0
            for user in user_data:
                total_age += user['age']
            average_age = total_age / len(user_data)
            print(f"Средний возраст пользователей: {average_age}")

    elif choice == '5':
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")
