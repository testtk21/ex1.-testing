#Абдулаев Абакар
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
        if not name.isalpha:
            print("ошибка, имя должно содержать буквы")
        

        user_data.append({'name': name, 'age': age})
    elif choice == '2':
        name=input("Введите имя удаляемого пользователя: ")
        for i in user_data:
            name==i
            user_data.remove(i)
    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")
    elif choice == '4':
        x=0
        for i in user_data:
            x += i['age']
        srednee=x/len(user_data)
        print("Средний возраст равен: ", srednee)


    elif choice == '5':
        print("Выход из программы.")
        break
