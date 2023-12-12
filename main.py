user_data = []

while True:
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("2. Вывести информацию о пользователях")
    print("4. Вычислить средний возраст")
    print("5. Выйти")
    # ЧТОТОТОТЧОЧТОЧТОЧ
    choice = input("Выберите действие (1/2/3/4/5): ")

    if choice == '1':
        name = input("Введите имя пользователя: ")
        age = input("Введите возраст пользователя: ")
        try:
            name=str(name)
            age=int(age)
        except ValueError:
            print("Ошибка неверный формат возвраста или имени")
            continue

        user_data.append({'name': name, 'age': age})

    elif choice =='2':
        name = input("Введите имя пользователя для удаления:")
        for user in user_data:
            if user['name'] == name:
                user_data.remove(user)
                print(f"Пользователь {name} удален")
                break
            
    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {name}, Возраст: {age}")

    elif choice == '4':
        if len(user_data) == 0:
            print("Нет данных о пользователе")
        else:
            total_age =0
            for user in user_data:
                total_age += user['age']
                average_age = total_age / len(user_data)
                print(f"Средний возвраст пользователей: {average_age}")

    elif choice == '5':
        print("Выход из программы.")
        break
