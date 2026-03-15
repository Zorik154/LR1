from components.autoservice import AutoService


def main() -> None:
    FILE_PATH: str = "autoservice.json"
    service: AutoService = AutoService(FILE_PATH)

    while True:
        print("\nМеню Автомастерской:")
        print("1. Показать автомобили")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Выход")
        choice: str = input("Выберите действие: ")

        if choice == "1":
            service.show_cars()
        elif choice == "2":
            service.add_car()
        elif choice == "3":
            service.delete_car()
        elif choice == "4":
            service.save_data()
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
