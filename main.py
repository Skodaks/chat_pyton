import time  # подключить модуль "time"
from datetime import datetime  # подключаем модуль datetime и из него берем него класс datetime (одноименный)


# time - чтобы получать текущее время
# datetime - чтобы выводить время в человекочитаемом формате
# time.time() - текущее время в формате unix timestamp - это количество секунд

# Функция умеет выводить сообщение на экран
def print_message(msg):
    readable_time = datetime.fromtimestamp(msg['time'])  # с помощью datetime получаем время в читаемом формате
    print(f"{msg['name']} / {readable_time}")  # вывести на экран имя и время из сообщения
    print(msg["text"])  # Выводим текст сообщения


def add_message(name, text):
    new_message = {  # создаем новый словарь
        "name": name,  # записываем туда поля name и text из тех данных, которые получила функция
        "text": text,
        "time": time.time()  # в поле time кладем текущее время
    }
    all_messages.append(new_message)  # в список сообщений добавим новое сообщение


all_messages = [  # В этом списке хранятся все сообщения чата
    {  # каждое сообщение это словарь с полями text, name и time
        "text": 'Привет всем в чате',
        "name": "Mike",
        "time": time.time() - 3600  # типа майк написал сообщение час (3600 сек) назад
    },
    {
        "text": "И тебе привет, Майк",
        "name": "Вася",
        "time": time.time() - 1800  # типа полчаса назад
    },
    {
        "text": "Ой ребята, как тут все здорово",
        "name": "Ксения",
        "time": time.time() - 60
    },
]

add_message("Mike", "Все я устал, иду спать")
add_message("Вася", "Спокойной ночи")
add_message("Петя", "Привет всем")
for message in all_messages:  # цикл for пройдет по всем сообщения
    print_message(message)  # каждое сообщение напечатаем
    print("—" * 25)  # напечатаем 25 тире чтобы создать линию под сообщением (для красоты)essage(message2)