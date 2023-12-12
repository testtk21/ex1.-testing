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
        age = int(input("Введите возраст пользователя: "))
        user_data.append({'name': name, 'age': age})
    elif choice == '2':
        name_to_delete = input("Введите имя пользователя для удаления: ")
        for user in user_data:
            if user['name'] == name_to_delete:
                user_data.remove(user)
                print(f"Пользователь {name_to_delete} удален")
                break
        else:
            print(f"Пользователь {name_to_delete} не найден")
    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")
    elif choice == '4':
        if len(user_data) > 0:
            total_age = sum(user['age'] for user in user_data)
            average_age = total_age / len(user_data)
            print(f"Средний возраст: {average_age}")
        else:
            print("Нет информации для вычисления среднего возраста")
    elif choice == '5':
        print("Выход из программы.")
        break
