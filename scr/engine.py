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
            2: ["Просмотр ВСЕХ записей в телефонном справочнике", self.all_phone],
            3: ["Добавление новой записи в телефонный справочник", self.add_note],
            4: ["Редактирование имеющейся записи", self.editing_post],
            5: ["Поиск записей по одной или нескольким характеристикам", self.search],
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

    def _show_one_line(self, line: list):
        '''
        вывод одной форматированной строки
        :param line:
        :return: None
        '''
        print('{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}'.format(
            *line)
        )

    def _check_line(self, line: list) -> bool:
        '''
        проверка правильности заполнения данных в полях справочника
        :param line:
        :return: bool
        '''
        flag = True  # TODO сделать еще проверки
        result = [(len(x) <= 15) for x in line]  # проверка длинны не более 15 символов
        if not bool(all(result)):
            flag = False
        return flag

    def all_phone(self):
        '''
        вывод всего телефонного справочника
        :return: None
        '''
        self._show_one_line(line=self.head)
        for line in self.table:
            self._show_one_line(line=line)

    def add_note(self):
        '''
        Добавление новой записи в справочник
        проверка на длинну записи
        :return: None
        '''
        print(
            "Добавьте данные\nфамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)\n"
            "не более 15 символов")

        while True:
            family, name, surname, organization, phone_working, phone_personal = input("family: "), input(
                "name: "), input(
                "surname: "), input("organization: "), input("phone_working: "), input("phone_personal: ")
            line = [family, name, surname, organization, phone_working, phone_personal]

            if self._check_line(line=line):  # проверка правильности заполнения данных
                self.table.append(line)
                break
            print("значения должны быть не более 15 символов")

        with open(self.path_db, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.head)  # запись заголовков
            for row in self.table:  # запись строк
                writer.writerow(row)

    def search(self) -> list:
        '''
        Поиск записей по одной или нескольким характеристикам
        :return: список номеров строк с совпадающими записями
        '''
        result = list()

        family = input("наберите фамилию, или нажмите ввод: ")
        name = input("наберите имя, или нажмите ввод: ")
        surname = input("наберите фамилию, или нажмите ввод: ")
        organization = input("наберите организацию, или нажмите ввод: ")
        phone_working = input("наберите рабочий телефон, или нажмите ввод: ")
        phone_personal = input("наберите личный телефон, или нажмите ввод: ")

        search_list = [family, name, surname, organization, phone_working, phone_personal]
        number_list = list()

        for number, line in enumerate(self.table):
            res_bool = any(map(lambda x: x[0].lower() == x[1].lower(), zip(line, search_list)))
            if res_bool:
                result.append(line)
                number_list.append(number)

        print('Количество найденных записей: {}'.format(len(result)))
        for line in result:
            self._show_one_line(line=line)

        return number_list

    def editing_post(self):
        '''
        редактироване имеющейся записи в телефонном справочнике
        :return: None
        '''
        pass

    def run(self, number: int):
        '''
        запускает выполнение метода класса по порядковому номеру
        :param number:
        :return:
        '''
        self.commands_to_execute.get(number)[1]()


if __name__ == "__main__":
    phone_book = Phonebook()
    phone_book.run(number=4)
