from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import start, button, handle_message
from config import TOKEN

# Создание приложения - Creating an application
application = Application.builder().token(TOKEN).build()

# Регистрация обработчиков - Handler registration
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))
application.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, handle_message))

# Запуск бота - Starting the bot
if __name__ == "__main__":
    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    application.run_polling()