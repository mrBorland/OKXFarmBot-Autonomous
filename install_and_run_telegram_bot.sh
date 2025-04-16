#!/bin/bash

echo "[+] Оновлення системи та встановлення залежностей..."
apt update && apt install -y build-essential gcc python3-dev libffi-dev libssl-dev python3-pip

echo "[+] Оновлення pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

echo "[+] Встановлення aiogram 2.25.1..."
pip install aiogram==2.25.1

echo "[+] Запуск Telegram-бота..."
python3 /root/OKXFarmBot/telegram_bot.py
