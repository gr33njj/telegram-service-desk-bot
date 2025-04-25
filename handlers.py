import logging
import os
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_main_menu, get_computer_menu, get_mfu_menu, get_edo_menu, get_confirm_menu, get_description_menu
from config import CHANNEL_ID

# Настройка логирования - Configuring logging
logging.basicConfig(filename="logs/bot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Хранилище данных пользователей - User data storage
user_data = {}

# Команда /start - The /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋 Я бот техподдержки. Выбери категорию:",
        reply_markup=get_main_menu()
    )
    logging.info(f"User {user.id} started bot")

# Обработка нажатий на кнопки - Keystroke processing
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id  

    # Категории - Categories
    if query.data == "computer":
        user_data[user_id] = {"category": "Компьютер"}
        await query.edit_message_text("Выбери проблему:", reply_markup=get_computer_menu())
    elif query.data == "mfu":
        user_data[user_id] = {"category": "МФУ"}
        await query.edit_message_text("Выбери проблему:", reply_markup=get_mfu_menu())
    elif query.data == "edo":
        user_data[user_id] = {"category": "ЭДО"}
        await query.edit_message_text("Выбери проблему:", reply_markup=get_edo_menu())
    elif query.data == "other":
        user_data[user_id] = {"category": "Другое", "subcategory": "Другое"}
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())

    # Подкатегории для Компьютера - Subcategories for Computer
    elif query.data == "comp_power":
        user_data[user_id]["subcategory"] = "Не включается"
        await query.edit_message_text("Опиши проблему, на какой операционной системе она возникла? (Windows или Astra Linux?) (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "comp_slow":
        user_data[user_id]["subcategory"] = "Медленно работает"
        await query.edit_message_text("Опиши проблему, она связанна с работой в браузере или с другим программным обеспечением? (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "comp_net":
        user_data[user_id]["subcategory"] = "Проблемы с интернетом"
        await query.edit_message_text("Опиши проблему, где возникают трудности с загрузкой? (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "comp_other":
        user_data[user_id]["subcategory"] = "Другое"
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())

    # Подкатегории для МФУ - Subcategories for MFPs
    elif query.data == "mfu_jam":
        user_data[user_id]["subcategory"] = "Замятие бумаги"
        await query.edit_message_text("Опиши проблему, на каком МФУ она возникла? (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "mfu_quality":
        user_data[user_id]["subcategory"] = "Плохое качество печати"
        await query.edit_message_text("Опиши проблему, на каком МФУ она возникла? В картридже есть тонер или требуется замена? (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "mfu_connect":
        user_data[user_id]["subcategory"] = "Не печатает"
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "mfu_other":
        user_data[user_id]["subcategory"] = "Другое"
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())

    # Подкатегории для ЭДО - Subcategories for EDI
    elif query.data == "edo_pass":
        user_data[user_id]["subcategory"] = "Неверный пароль"
        await query.edit_message_text("Опиши проблему, у какого пользователя она возникла (ФИО, отдел) (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "edo_block":
        user_data[user_id]["subcategory"] = "Учетная запись заблокирована"
        await query.edit_message_text("Опиши проблему, у какого пользователя она возникла (ФИО, отдел) (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "edo_sign":
        user_data[user_id]["subcategory"] = "Проблема с подписью"
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())
    elif query.data == "edo_other":
        user_data[user_id]["subcategory"] = "Другое"
        await query.edit_message_text("Опиши проблему, по желанию можно прикрепить фото или скриншот (ОБЯЗАТЕЛЬНО УКАЖИ КАК С ТОБОЙ СВЯЗАТЬСЯ ИЛИ НОМЕР КАБИНЕТА, ГДЕ ТРЕБУЕТСЯ ПОМОЩЬ! ✏️):", reply_markup=get_description_menu())                
    # Добавьте аналогично для других подкатегорий... - Add similarly for other subcategories....
    
    # Возврат к главному меню - Return to the main menu
    elif query.data == "back_to_main":
        await query.edit_message_text("Выбери категорию:", reply_markup=get_main_menu())
        if user_id in user_data:
            del user_data[user_id]  # Очистка данных при возврате - Clearing data on return

    # Возврат к подкатегории (из описания) - Return to subcategory (from description)
    elif query.data == "back_to_subcategory":
        category = user_data[user_id]["category"]
        if category == "Компьютер":
            await query.edit_message_text("Выбери проблему:", reply_markup=get_computer_menu())
        elif category == "МФУ":
            await query.edit_message_text("Выбери проблему:", reply_markup=get_mfu_menu())
        elif category == "ЭДО":
            await query.edit_message_text("Выбери проблему:", reply_markup=get_edo_menu())
        else:
            await query.edit_message_text("Выбери категорию:", reply_markup=get_main_menu())
            del user_data[user_id]

    # Подтверждение или отмена - Confirm or cancel
    elif query.data == "send":
        data = user_data[user_id]
        # Чтение последнего ticket_id из файла - Read last ticket_id from file
        ticket_file = "ticket_id.txt"
        if os.path.exists(ticket_file):
            with open(ticket_file, "r") as f:
                ticket_id = int(f.read().strip()) + 1
        else:
            ticket_id = 1
        # Сохранение нового ticket_id - Saving a new ticket_id
        with open(ticket_file, "w") as f:
            f.write(str(ticket_id))

        ticket_text = (
            f"Заявка #{ticket_id}\n"
            f"👤 Имя: {query.from_user.username or query.from_user.first_name}\n"
            f"🗂️ Категория: {data['category']} -> {data['subcategory']}\n"
            f"📝 Описание: {data.get('description', 'нет')}\n"
            f"🏢 Кабинет: {data.get('room', 'не указан')}\n"
            f"📸 Фото: {'есть' if data.get('photo') else 'нет'}"
        )
        await context.bot.send_message(chat_id=CHANNEL_ID, text=ticket_text)
        if data.get("photo"):
            await context.bot.send_photo(chat_id=CHANNEL_ID, photo=data["photo"])
        await query.edit_message_text(f"Заявка #{ticket_id} отправлена! ✅")
        logging.info(f"Ticket #{ticket_id} sent by {user_id}")
        del user_data[user_id]  # Очистка данных - Data cleansing
    elif query.data == "cancel":
        await query.edit_message_text("Заявка отменена. Начать заново? /start")
        del user_data[user_id]

# Обработка текстовых сообщений и фото - Processing of text messages and photos
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in user_data:
        if update.message.text:
            if update.message.text.lower() == "пропустить":
                user_data[user_id]["description"] = "нет"
            else:
                user_data[user_id]["description"] = update.message.text
        if update.message.photo:
            user_data[user_id]["photo"] = update.message.photo[-1].file_id
        await update.message.reply_text("Проверь и отправь заявку:", reply_markup=get_confirm_menu())