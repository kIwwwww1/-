"""Задача: Анализ логов
    Ты получил файл logs.txt, в котором хранятся записи о событиях в формате:
        2023-10-05 14:23:17 | ERROR | Не удалось подключиться к базе данных
        2023-10-05 14:24:01 | INFO | Пользователь 'admin' вошёл в систему
        2023-10-05 14:25:44 | WARNING | Низкое место на диске

Каждая строка содержит:

    Время события (в формате YYYY-MM-DD HH:MM:SS)
    Уровень события (INFO, WARNING, ERROR)
    Сообщение

Напиши программу на Python, которая:

    1 Прочитает файл logs.txt.
    2 Подсчитает количество записей для каждого уровня логирования (INFO, WARNING, ERROR).
    3 Найдёт и выведет самое частое сообщение среди ERROR логов.
    4 Сохранит все ERROR логи в отдельный файл errors_only.txt."""

from statistics import mode


class ReadFile:
    all_error = []
    f = open("logs.txt", mode="r", encoding="utf-8")

    @classmethod
    def read_file(cls, file):
        with f:
            with open("errors_only.txt", "w", encoding="utf-8") as f1:
                for line in f.readlines():
                    f1.write(line)
                    one_line = line.split("|")
                    cls.all_error.append(one_line)

    @classmethod
    def get_error(cls):
        info = 0
        warning = 0
        error = 0
        for er in ReadFile.all_error:
            match er[1].strip().lower():
                case "info":
                    info += 1
                case "warning":
                    warning += 1
                case _:
                    error += 1
        return f"INFO: {info}, WARNING: {warning}, ERROR: {error}"

    @classmethod
    def get_max_message(cls):
        main_list = mode([i[2] for i in cls.all_error]).strip()
        return main_list


# Наш файл
f = open("logs.txt", mode="r", encoding="utf-8")
# Действие
ReadFile.read_file(f)
print(ReadFile.get_error())
print(ReadFile.get_max_message())
