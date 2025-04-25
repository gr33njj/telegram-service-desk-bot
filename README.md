# Service Desk Telegram Bot [EN] 
## is a convenient tool for automating the processing of technical requests from company employees. The bot allows users to quickly create support requests, select problem categories, attach descriptions and files (screenshots, photos), and track the status of requests.

🔹 Main functions
📌 For users (you can edit for yourself):
✅ Select a problem category (Computer, MFP, EDI, Other)
✅ Refine the subcategory (e.g., “Does not turn on”, “Slow”, “Internet problems”)
✅ Adding a description of the problem (text + possibility to attach a file)
✅ Confirming and sending the request
✅ Receiving notifications about request status (in progress, completed)

📌 For administrators:
🛠 Viewing all requests
🛠 Changing the status (open, in progress, completed) [in development]
🛠 Adding comments to requests [in development]
🛠 Notifications of new requests

# Service Desk Telegram Bot [RU]
## это удобный инструмент для автоматизации обработки технических заявок сотрудников компании. Бот позволяет пользователям быстро создавать заявки в службу поддержки, выбирать категории проблем, прикреплять описание и файлы (скриншоты, фото), а также отслеживать статус заявок.

🔹 Основные функции
📌 Для пользователей (можно редактировать под себя):
✅ Выбор категории проблемы (Компьютер, МФУ, Электронный документооборот, Другое)
✅ Уточнение подкатегории (например, "Не включается", "Медленно работает", "Проблемы с интернетом")
✅ Добавление описания проблемы (текст + возможность прикрепить файл)
✅ Подтверждение и отправка заявки
✅ Получение уведомлений о статусе заявки (в работе, выполнено)

📌 Для администраторов:
🛠 Просмотр всех заявок
🛠 Изменение статуса (открыта, в работе, выполнена) [в разработке]
🛠 Добавление комментариев к заявкам [в разработке]
🛠 Уведомления о новых заявках

# ServiceDeskBot

## Как запустить бота

1. Установите Python 3.12.6 с https://www.python.org/downloads/.
2. Откройте терминал в папке `ServiceDeskBot`.
3. Установите библиотеку: `pip install python-telegram-bot==20.7`.
4. В `config.py` укажите:
   - `TOKEN` — токен от @BotFather.
   - `CHANNEL_ID` — ID канала или группы.
5. Запустите бота: `python main.py`.
6. Откройте Telegram, найдите бота и напишите `/start`.

## Остановка
Нажмите Ctrl+C в терминале.


## How to start the bot

1. Install Python 3.12.6 from https://www.python.org/downloads/.
2. Open a terminal in the `ServiceDeskBot` folder.
3. Install the library: `pip install python-telegram-bot==20.7`.
4. In `config.py` specify:
   - `TOKEN` - token from @BotFather.
   - `CHANNEL_ID` - the ID of the channel or group.
5. Start the bot: `python main.py`.
6. Open Telegram, find the bot and write `/start`.

## Stop
Press Ctrl+C in the terminal.
