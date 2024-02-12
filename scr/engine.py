import csv
from icecream import ic


class Phonebook:
    path_db = "./db_phone.csv"

    def __init__(self):
        with open(self.path_db, encoding='utf-8') as file:
            self.table = list()
            for line in csv.reader(file, delimiter=',', quotechar='"'):
                self.head = line
                break
            for line in csv.reader(file, delimiter=',', quotechar='"'):
                self.table.append(line)

        self.commands_to_execute = {
            1: ["Список вызываемых команд", self.help],
            2: ["Посмотреть ВСЕ записи в телефонном справочнике", self.all_phone],
            3: ["", ""],
            4: ["", ""],
        }

    def welcome(self):
        '''
        приветствие пользователя
        :return: None
        '''
        print("Welcome to the phonebook!")

    def help(self):
        '''
        возвращает возможные команды
        :return: None
        '''
        for key, volume in self.commands_to_execute.items():
            print(f'{key}:  {volume[0]}')

    def show_one_line(self, line: list):
        '''
        вывод одной форматированной строки
        :param line:
        :return: None
        '''
        print('{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}'.format(
            *line)
        )

    def all_phone(self):
        '''
        вывод всего телефонного справочника
        :return: None
        '''
        self.show_one_line(line=self.head)
        for line in self.table:
            self.show_one_line(line=line)

    def run(self, number):
        '''
        запускает выполнение метода класса по порядковому номеру
        :param number:
        :return:
        '''
        self.commands_to_execute.get(number)[1]()


if __name__ == "__main__":
    phone_book = Phonebook()
    phone_book.run(number=2)
