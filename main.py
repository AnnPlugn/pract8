import csv
from prettytable import PrettyTable

import db
import universal


def create_csv_file():
    with open('Egor-1point.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID студента", "№ группы", "ФИО", "Средний балл", "№ зачетной книжки"])
        for i in range(1):
            id = i +1
            while True:
                try:
                    full_name = input("Введите ФИО: ")
                    stu_numb = int(input("Введите № зачетной книжки: "))
                    group_name = int(input("Введите № группы: "))
                    average_mark = int(input("Введите средний балл успеваемости (от 0 до 5): "))
                    if 0 < average_mark <= 5:
                        writer.writerow([id, group_name, full_name, average_mark, stu_numb])
                        break
                    else:
                        print('Your average_mark should be from 0 to 5')
                except ValueError:
                    print("Oops! That was no valid number. Try again...")
                except TypeError:
                    print("Oops! That was no valid number. Try again...")
                writer.writerow([id, group_name, full_name, average_mark, stu_numb])
    print("Файл успешно создан и заполнен данными!")

def read_csv_file():
    table = PrettyTable(["ID студента", "№ группы", "ФИО", "Средний балл", "№ зачетной книжки"])
    with open('Egor-1point.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            table.add_row(row)
            db.save_result(row[0],row[1],row[2],row[3])
            print(row)
    print(table)

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Ввести данные об учащемся, результат сохранить в MySQL.
3. Вывести в консоль промеж результат
4. Сохранить все данные из MySQL в Excel.
5. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, create_csv_file, read_csv_file,
                            db.save_db_to_xlsx)
    return


if __name__ == '__main__':
    main()
