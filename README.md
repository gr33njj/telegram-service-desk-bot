# 🚀 Service Desk Telegram Bot [EN]

**Service Desk Telegram Bot** is a convenient tool for automating the processing of technical requests of company employees via Telegram. The bot allows you to quickly create, track and manage service desk requests.

## 🌟 Main functions

### 👨‍💻 For users
- 📋 Select problem category (Computer, MFP, EDI, Other)
- 🔍 Refine the subcategory (e.g., “Does not turn on”, “Slow”)
- ✏️ Add a description of the problem with an option to attach files
- ✅ Confirming and submitting the request
- 🔔 Notifications about request status (in progress/completed)

### 👨‍🔧 For administrators
- 📊 View all requests
- 🛠 Change request status [in progress]
- 💬 Adding comments to requests [in development]
- 🔔 Notifications of new applications

# 🚀 Service Desk Telegram Bot [RU]

**Service Desk Telegram Bot** – это удобный инструмент для автоматизации обработки технических заявок сотрудников компании через Telegram. Бот позволяет быстро создавать, отслеживать и управлять заявками в службе поддержки.

## 🌟 Основные функции

### 👨‍💻 Для пользователей
- 📋 Выбор категории проблемы (Компьютер, МФУ, ЭДО, Другое)
- 🔍 Уточнение подкатегории (например, "Не включается", "Медленно работает")
- ✏️ Добавление описания проблемы с возможностью прикрепления файлов
- ✅ Подтверждение и отправка заявки
- 🔔 Уведомления о статусе заявки (в работе/выполнено)

### 👨‍🔧 Для администраторов
- 📊 Просмотр всех заявок
- 🛠 Изменение статуса заявок [в разработке]
- 💬 Добавление комментариев к заявкам [в разработке]
- 🔔 Уведомления о новых заявках

# Launch

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
