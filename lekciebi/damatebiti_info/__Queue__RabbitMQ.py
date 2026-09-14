# RabbitMQ — это брокер сообщений (message broker), который работает с очередями сообщений.

# RabbitMQ — это не обычная структура данных внутри твоего Python-кода.
# Это отдельный message broker, который принимает сообщения от одной программы и передаёт их другой.

# Например, в будущем в системе GeorgianAirlink может быть:

                    # CRM
                    #  │
                    #  │ "Создан новый клиент"
                    #  ▼
                    # RabbitMQ
                    #  │
                    #  ├──► Billing
                    #  │
                    #  ├──► Network Provisioning
                    #  │
                    #  └──► Notification Service

# То есть одна система создаёт сообщение, RabbitMQ принимает его, а другой сервис обрабатывает.
# В обычном deque:
# Если программа завершилась, обычный deque исчезает вместе с процессом.
# Он предназначен для обмена сообщениями между приложениями и сервисами, а не просто для хранения элементов в Python-коллекции.


# Queue - რიგის პრინციპია.
# ჩვეულებრივ მუშაობს FIFO პრინციპით:
# First In, First Out.

# deque - Python-ის მონაცემთა სტრუქტურაა,
# რომელიც საშუალებას გვაძლევს ელემენტები
# დავამატოთ და წავშალოთ ორივე მხრიდან.

# RabbitMQ - შეტყობინებების ბროკერია.
# ის გამოიყენება სხვადასხვა პროგრამებსა
# და სერვისებს შორის შეტყობინებების გადასაცემად.



# RabbitMQ — отдельный сервер:
# Python App A
#      ↓
#   RabbitMQ
#      ↓
# Python App B

# Python программа
#       │
#       ▼
#     deque
#       │
#    RAM процесса
#--------------------------


# Producer
#    ↓
# RabbitMQ
#    ↓
#  Queue
#    ↓
# Consumer


# Например:

# Интернет-магазин
#       ↓
# "Новый заказ"
#       ↓
#    RabbitMQ
#       ↓
#     Queue
#       ↓
# Сервис обработки заказов

# Queue — очередь. Queue — это прежде всего принцип организации данных.
# Обычно очередь работает по принципу FIFO:
# First In → First Out — кто первый вошёл, тот первый вышел.
            # Nika → Ana → Giorgi

            # выходит Nika
            # потом Ana
            # потом Giorgi

# В Python такую очередь можно сделать через deque: deque — инструмент Python . deque означает Double-Ended Queue — двусторонняя очередь.
# Она позволяет работать с обоими концами:

            # from collections import deque

            # queue = deque()

            # queue.append("Nika")
            # queue.append("Ana")
            # queue.append("Giorgi")

            # print(queue.popleft())  # Nika
            # print(queue.popleft())  # Ana

# То есть:

            #      deque
            #     ←             →
            #  начало         конец
            #     ↓             ↓
            #   [10, 20, 30, 40]

# Поэтому deque можно использовать не только как Queue, но и как Stack.


# from collections import deque

# queue = deque()

# queue.append("Nika")
# queue.append("Ana")
# queue.append("Giorgi")

# print(queue.popleft())

# Здесь действует принцип FIFO:

# First In → First Out
# первый вошёл → первый вышел

# from collections import deque

# # queue არის რიგის მონაცემთა სტრუქტურა.
# # იგი მუშაობს FIFO პრინციპით:
# # First In, First Out
# # ვინც პირველი დაემატა, ის პირველი გამოვა.

# queue = deque()

# # რიგის ბოლოში ვამატებთ ელემენტებს.
# queue.append("Nika")
# queue.append("Ana")
# queue.append("Giorgi")

# # popleft() რიგიდან პირველ ელემენტს იღებს და შლის.
# print(queue.popleft())