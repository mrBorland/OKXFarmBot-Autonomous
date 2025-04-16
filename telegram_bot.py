
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

# Дані користувача
BOT_TOKEN = "7626770291:AAG3UC1h3vt1aR9h0ALAqg3oo9RlvsMGSzI"
CHAT_ID = 6821675571

# Ініціалізація бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Кнопки меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("🚀 Фармити"))
main_menu.row(KeyboardButton("💰 Баланс"), KeyboardButton("📤 Вивести"))
main_menu.row(KeyboardButton("📊 Статистика"), KeyboardButton("⚙️ Статус акаунтів"))
main_menu.row(KeyboardButton("🔁 Перезапуск"), KeyboardButton("📂 Експорт логів"))

# /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привіт, Тоні! Обери дію:", reply_markup=main_menu)

# 🚀 Фарм
@dp.message_handler(lambda message: message.text == "🚀 Фармити")
async def handle_farm(message: types.Message):
    await message.answer("Запускаю фарм...")
    os.system("python3 main.py")

# 💰 Баланс
@dp.message_handler(lambda message: message.text == "💰 Баланс")
async def handle_balance(message: types.Message):
    await message.answer("Перевіряю баланс...")
    os.system("python3 check_balance.py")

# 📤 Вивести
@dp.message_handler(lambda message: message.text == "📤 Вивести")
async def handle_withdraw(message: types.Message):
    await message.answer("Виводжу USDT з акаунтів...")
    os.system("python3 withdraw.py")

# 📊 Статистика
@dp.message_handler(lambda message: message.text == "📊 Статистика")
async def handle_stats(message: types.Message):
    await message.answer("Поки що не реалізовано. Незабаром!")

# ⚙️ Статус акаунтів
@dp.message_handler(lambda message: message.text == "⚙️ Статус акаунтів")
async def handle_status(message: types.Message):
    await message.answer("Перевірка статусу акаунтів (в розробці)...")

# 🔁 Перезапуск
@dp.message_handler(lambda message: message.text == "🔁 Перезапуск")
async def handle_restart(message: types.Message):
    await message.answer("Перезапускаю бота...")
    os.system("systemctl restart okxfarmbot")

# 📂 Експорт логів
@dp.message_handler(lambda message: message.text == "📂 Експорт логів")
async def handle_logs(message: types.Message):
    log_path = "/root/OKXFarmBot/logs.txt"
    if os.path.exists(log_path):
        await message.answer_document(open(log_path, "rb"))
    else:
        await message.answer("Логів поки немає або файл не знайдено.")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
