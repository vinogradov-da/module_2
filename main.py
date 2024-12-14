from task_1 import Smartphone, Automobile, Table

if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 12", 256)
    car = Automobile("Audi A6", "белый", 60)
    folding_table = Table(70, 150)

    try:
        phone.set_memory(-124)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        car.change_speed(-100)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
     folding_table.increase_length(-45)
    except ValueError:
        print('Ошибка: неправильные данные')
