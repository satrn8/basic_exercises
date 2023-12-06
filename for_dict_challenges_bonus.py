"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def max_message_id(dates):
    # Вывести айди пользователя, который написал больше всех сообщений
    number = []  # добавляю все "sent_by" - количество отправленных сообщений пользователем
    for user in dates:
        sent_message = user["sent_by"]
        number.append(sent_message)
    max_sent = max(number)  # максимальное значение

    id_send = {}  # создаю новый словарь, в него добавлю id пользователя и количество отправленных им сообщений
    for ui in dates:
        ui2 = ui["id"]
        sent2 = ui["sent_by"]
        id_send[ui2] = sent2

    for key, value in id_send.items():  # перебираю ключи по значениям, сравнивая значения с максимальным количеством отправленных сообщений
        if value == max_sent:
            print(f"{key} пользователь который написал больше всех сообщений")  # вывожу пользователей, которые отправили сообщения совпадающее с максимально полученным значением по всем пользователям


def max_see_id(dates):
    # Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей
    number = []
    id_seen = {}

    for user in dates:
        ui2 = user["id"]
        sent_message = user["seen_by"]
        len_seen_messages = len(sent_message)
        id_seen[ui2] = len_seen_messages
        number.append(len(sent_message))
    max_number = max(number)

    for key, value in id_seen.items():  # перебираю ключи по значениям, сравнивая значения с максимальным количеством отправленных сообщений
        if value == max_number:
            print(f"{key} пользователь, сообщения которого видело больше всего уникальных пользователей.")  # вывожу пользователей, которые отправили сообщения совпадающее с максимально полученным значением по всем пользователям


def time_messages(dates):
    # Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов)
    before_noon = 0
    after_noon = 0
    evening = 0
    for user in dates:
        time_user = user["sent_at"]
        hour_answer = time_user.time()
        if hour_answer < datetime.time(hour=12, minute=00, second=00, microsecond=0, tzinfo=None, fold=0):
            before_noon += 1
        elif hour_answer > datetime.time(hour=12, minute=00, second=00, microsecond=0, tzinfo=None, fold=0) and hour_answer < datetime.time(hour=18, minute=00, second=00, microsecond=0, tzinfo=None, fold=0):
            after_noon += 1
        else:
            evening += 1

    if before_noon > after_noon and before_noon > evening:
        print(f"Больше всего сообщений было утром {before_noon}")
    elif after_noon > before_noon and after_noon > evening:
        print(f"Больше всего сообщений было днем {after_noon}")
    else:
        print(f"Больше всего сообщений было вечером {evening}")



if __name__ == "__main__":
    dates = generate_chat_history()
    max_message_id(dates)
    max_see_id(dates)
    time_messages(dates)
