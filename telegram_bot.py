from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

# РќРѕРІРёР№ С‚РѕРєРµРЅ
BOT_TOKEN = "7567566641:AAGKaV2Qx5GrhXx_a2Juh7KrlvJIRVRX1M8"
CHAT_ID = 6821675571

# Р†РЅС–С†С–Р°Р»С–Р·Р°С†С–СЏ Р±РѕС‚Р°
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# РњРµРЅСЋ
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("рџљЂ Р¤Р°СЂРјРёС‚Рё"))
main_menu.row(KeyboardButton("рџ’° Р‘Р°Р»Р°РЅСЃ"), KeyboardButton("рџ“¤ Р’РёРІРµСЃС‚Рё"))
main_menu.row(KeyboardButton("рџ“Љ РЎС‚Р°С‚РёСЃС‚РёРєР°"), KeyboardButton("вљ™пёЏ РЎС‚Р°С‚СѓСЃ Р°РєР°СѓРЅС‚С–РІ"))
main_menu.row(KeyboardButton("рџ”Ѓ РџРµСЂРµР·Р°РїСѓСЃРє"), KeyboardButton("рџ“‚ Р•РєСЃРїРѕСЂС‚ Р»РѕРіС–РІ"))

# РљРѕРјР°РЅРґРё
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("РџСЂРёРІС–С‚, РўРѕРЅС–! РћР±РµСЂРё РґС–СЋ:", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == "рџљЂ Р¤Р°СЂРјРёС‚Рё")
async def handle_farm(message: types.Message):
    await message.answer("Р—Р°РїСѓСЃРєР°СЋ С„Р°СЂРј...")
    os.system("python3 main.py")

@dp.message_handler(lambda message: message.text == "рџ’° Р‘Р°Р»Р°РЅСЃ")
async def handle_balance(message: types.Message):
    await message.answer("РџРµСЂРµРІС–СЂСЏСЋ Р±Р°Р»Р°РЅСЃ...")
    os.system("python3 check_balance.py")

@dp.message_handler(lambda message: message.text == "рџ“¤ Р’РёРІРµСЃС‚Рё")
async def handle_withdraw(message: types.Message):
    await message.answer("Р’РёРІРѕРґР¶Сѓ USDT Р· Р°РєР°СѓРЅС‚С–РІ...")
    os.system("python3 withdraw.py")

@dp.message_handler(lambda message: message.text == "рџ“Љ РЎС‚Р°С‚РёСЃС‚РёРєР°")
async def handle_stats(message: types.Message):
    await message.answer("РџРѕРєРё С‰Рѕ РЅРµ СЂРµР°Р»С–Р·РѕРІР°РЅРѕ. РќРµР·Р°Р±Р°СЂРѕРј!")

@dp.message_handler(lambda message: message.text == "вљ™пёЏ РЎС‚Р°С‚СѓСЃ Р°РєР°СѓРЅС‚С–РІ")
async def handle_status(message: types.Message):
    await message.answer("РџРµСЂРµРІС–СЂРєР° СЃС‚Р°С‚СѓСЃСѓ Р°РєР°СѓРЅС‚С–РІ (РІ СЂРѕР·СЂРѕР±С†С–)...")

@dp.message_handler(lambda message: message.text == "рџ”Ѓ РџРµСЂРµР·Р°РїСѓСЃРє")
async def handle_restart(message: types.Message):
    await message.answer("РџРµСЂРµР·Р°РїСѓСЃРєР°СЋ Р±РѕС‚Р°...")
    os.system("systemctl restart telegram_bot")

@dp.message_handler(lambda message: message.text == "рџ“‚ Р•РєСЃРїРѕСЂС‚ Р»РѕРіС–РІ")
async def handle_logs(message: types.Message):
    log_path = "/root/OKXFarmBot/logs.txt"
    if os.path.exists(log_path):
        await message.answer_document(open(log_path, "rb"))
    else:
        await message.answer("Р›РѕРіС–РІ РїРѕРєРё РЅРµРјР°С” Р°Р±Рѕ С„Р°Р№Р» РЅРµ Р·РЅР°Р№РґРµРЅРѕ.")

# Р—Р°РїСѓСЃРє
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
