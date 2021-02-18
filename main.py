import csv
from collections.abc import Iterable

class call_history():

    def __init__(self,id,telephone_number,replied,first_name,last_name,date_next_call,info_next_call):
        """Конструктор класса Old_base
        """
        self.id = id
        self.replied = 0
        self.first_name = first_name
        self.last_name = last_name
        self.date_next_call = date_next_call
        self.info_next_call = info_next_call


class Old_base():
    """Родительский класс для класса Best_base"""

    def __init__(self):
        """Конструктор класса Old_base
        """
        self.data_base = []
        self.my_iterator = 0
    color = 'green'

    @staticmethod
    def read_from_file(data_base):
        """Функция считывает данные для словаря из файла.
        param: data_base - словарь
        """
        with open('data3.csv') as File:
            reader = csv.DictReader(File, delimiter=';')
            for row in reader:
                data_base.append(row)

    @staticmethod
    def write_to_file(data_base):
        """Функция записывает данные из словаря в файл.
        param: data_base - словарь
        """
        with open('data4.csv', 'w', newline='\n') as out_file:
            writer = csv.DictWriter(out_file, delimiter=';', fieldnames=(
            'number', 'telephone', 'replied', 'first_name', 'last_name', 'date_next_call', 'info_next_call'))
            writer.writeheader()
            for row in data_base:
                writer.writerow(row)


class Best_base(Old_base):
    """ Этот класс создаёт словарь, а также методы для взаимодейстия со словарём.
    """

    def __init__(self):
        """Конструктор класса Best_base
        """
        super().__init__()

    def output_data_base(self, num):
        """Функция выводит словарь в консоль.
        param: num - параметр для вывода строк
        """
        for i in self.data_base:
            print(i)

    def using_iterator_and_generator(self):
        """Функция создаёт итератор и генератор, а потом совершает с ними работу.
        """
        print("Длина = ", len(self.data_base))
        my_list = []
        for i in range(len(self.data_base)):
            my_list.append(int(self.data_base[i]['number']))
        self.my_iterator = iter(my_list)
        print(next(self.my_iterator), next(self.my_iterator), next(self.my_iterator))
        # генератор
        print('Генератор:')
        my_generator = (int(x) * 2 for x in my_list)
        print(next(my_generator), next(my_generator), next(my_generator))

    def __repr__(self):
        """Функция возвращает определённое значение, когда в неё передаётся экземпляр класса.
        """
        return str(self.data_base[2]['telephone'])

    def __getitem__(self, item):
        """Функция получает индекс элемента, а потом возвращает элемент списка под этим номером.
        """
        return self.data_base[item]['first_name']

    def __setattr__(self, attr, value):
        """Вызывается при попытке присвоения полю экземпляра класса какого-либо значения. Производит проверку на тип данных.
        param: attr - имя атрибута
        param: value - значение, которое должно быть присвоено атрибуту
        """
        if isinstance(value, list):
            self.__dict__[attr] = value
        elif isinstance(value, Iterable):
            self.__dict__[attr] = value
        elif value > -1:
            self.__dict__[attr] = value
        else:
            raise (AttributeError, attr + ' not allowed')


def main():
    """Функция создаёт экземпляр класса Best_base. Записывает данные из файла в поля экзмепляра класса.
    Производится взаимодействие с экзепляром класса. Вызываются  все необходимые методы. Данные записываются в файл.
    """
    base = Best_base()
    base.read_from_file(base.data_base)
    base.output_data_base(-1)
    base.using_iterator_and_generator()
    select_path = int(input("Введите (1), чтобы выполнить сортировку по строковому полю.\nВведите (2), чтобы выполнить сортировку по числовому полю.\nВведите (4), если хотите использовать getitem.\nВведите (5), если хотите использовать rerp.\nВвод: "))
    if (select_path == 1):
        base.data_base.sort(key=lambda i: i['info_next_call'])
        base.output_data_base(base.data_base)
    elif (select_path == 2):
        base.data_base.sort(key=lambda i: int(i['number']))
        base.output_data_base(-1)
    elif (select_path == 3):
        b = input('Введите значение')
        base.__setattr__(base.color, b)
        print(base.color)
    elif (select_path == 4):
        choice_item = int(input("Введите число. Будет выведено имя под этим индексом.\nВвод:"))
        print("Использован getiem: ", base[choice_item])
    elif (select_path == 5):
        print("Использован repr: ", base)
    else:
        print("Введены некорректные данные!")
    select_save = int(input(
        "Введите (1), если хотите сделать сохранение.\nВвод: "))
    if (select_save == 1):
        base.write_to_file(base.data_base)


main()