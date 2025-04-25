from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Основное меню - Main menu
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("🖥️ Компьютер", callback_data="computer")],
        [InlineKeyboardButton("🖨️ МФУ", callback_data="mfu")],
        [InlineKeyboardButton("📝 ЭДО", callback_data="edo")],
        [InlineKeyboardButton("❓ Другое", callback_data="other")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Подменю для категории "Компьютер" - Submenu for the “Computer” category
def get_computer_menu():
    keyboard = [
        [InlineKeyboardButton("🔌 Не включается", callback_data="comp_power")],
        [InlineKeyboardButton("🐢 Медленно работает", callback_data="comp_slow")],
        [InlineKeyboardButton("🌐 Проблемы с интернетом", callback_data="comp_net")],
        [InlineKeyboardButton("❓ Другое", callback_data="comp_other")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Подменю для категории "МФУ" - Submenu for the “MFP” category
def get_mfu_menu():
    keyboard = [
        [InlineKeyboardButton("📄 Замятие бумаги", callback_data="mfu_jam")],
        [InlineKeyboardButton("🖨️ Плохое качество печати", callback_data="mfu_quality")],
        [InlineKeyboardButton("🔌 Не печатает", callback_data="mfu_connect")],
        [InlineKeyboardButton("❓ Другое", callback_data="mfu_other")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Подменю для категории "ЭДО" - Submenu for the “EDI” category
def get_edo_menu():
    keyboard = [
        [InlineKeyboardButton("🔑 Неверный пароль", callback_data="edo_pass")],
        [InlineKeyboardButton("🔒 Учетная запись заблокирована", callback_data="edo_block")],
        [InlineKeyboardButton("✍️ Проблема с подписью", callback_data="edo_sign")],
        [InlineKeyboardButton("❓ Другое", callback_data="edo_other")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Кнопки для подтверждения заявки - Buttons to confirm the application
def get_confirm_menu():
    keyboard = [
        [InlineKeyboardButton("✅ Отправить", callback_data="send"), InlineKeyboardButton("❌ Отмена", callback_data="cancel")],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_description_menu():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_subcategory")],
    ]
    return InlineKeyboardMarkup(keyboard)    