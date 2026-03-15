import json
import os
from typing import List, Dict

from components.cars import Car


class AutoService:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.cars: List[Car] = []
        self.load_data()

    def load_data(self) -> None:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data: List[Dict[str, str]] = json.load(f)
                    self.cars = [Car.from_dict(item) for item in data]
                print("Данные успешно загружены.")
            except json.JSONDecodeError:
                print("Ошибка чтения файла данных. Создан новый пустой список автомобилей.")
                self.cars = []
            except Exception as e:
                print(f"Ошибка при загрузке данных: {e}. Создан новый пустой список автомобилей.")
                self.cars = []
        else:
            print("Файл данных не найден. Создан новый пустой список автомобилей.")
            self.cars = []

    def save_data(self) -> None:
        try:
            data_to_save: List[Dict[str, str]] = [car.to_dict() for car in self.cars]
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)
            print("Данные успешно сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def show_cars(self) -> None:
        if not self.cars:
            print("Автомастерская пуста.")
            return

        print("Автомобили на обслуживании:")
        for i, car in enumerate(self.cars):
            print(f"{i + 1}. Модель: {car.Model}, Владелец: {car.Owner}")

    def add_car(self) -> None:
        model: str = input("Введите модель автомобиля: ")
        owner: str = input("Введите владельца автомобиля: ")

        new_car: Car = Car(model, owner)
        self.cars.append(new_car)
        print("Автомобиль добавлен.")

    def delete_car(self) -> None:
        if not self.cars:
            print("Автомастерская пуста. Удалять нечего.")
            return

        self.show_cars()
        try:
            index_str: str = input("Введите номер автомобиля для удаления: ")
            index: int = int(index_str)

            if 1 <= index <= len(self.cars):
                deleted_car: Car = self.cars.pop(index - 1)
                print(f"Автомобиль '{deleted_car.Model}' удалён.")
            else:
                print("Некорректный номер.")
        except ValueError:
            print("Некорректный ввод. Введите число.")
        except Exception as e:
            print(f"Ошибка при удалении автомобиля: {e}")