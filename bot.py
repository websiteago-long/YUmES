import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# ទាញយក Token ដោយសុវត្ថិភាពពី Render Environment Variables
TOKEN = os.getenv("TOKEN")

# បង្កើតប៊ូតុងម៉ឺនុយខាងក្រោម (Reply Keyboard)
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 គណនី"),
            KeyboardButton(text="🛍️ ទំនិញ")
        ],
        [
            KeyboardButton(text="🗂️ បញ្ជីទិញសរុប"),
            KeyboardButton(text="💰 ដាក់ប្រាក់")
        ],
        [
            KeyboardButton(text="⁉️ របៀបប្រើប្រាស់ Redeem Code")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="សូមជ្រើសរើសម៉ឺនុយខាងក្រោម..."
)

# ពេលអ្នកប្រើប្រាស់ផ្ញើ /start
async def cmd_start(message: Message):
    await message.answer(
        "🔥 សូមស្វាគមន៍មកកាន់ Cisy Shop Bot!",
        reply_markup=main_menu_keyboard
    )

# សារឆ្លើយតបពេលចុចលើប៊ូតុងនីមួយៗ
async def handle_account(message: Message):
    await message.answer("ព័ត៌មានគណនីរបស់អ្នកគឺ៖ ...")

async def handle_products(message: Message):
    await message.answer("បញ្ជីទំនិញដែលមានលក់៖ ...")

async def handle_history(message: Message):
    await message.answer("ប្រវត្តិនៃការបញ្ជាទិញរបស់អ្នក៖ ...")

async def handle_deposit(message: Message):
    await message.answer("សូមផ្ញើរូបភាពវិក្កយបត្រដើម្បីដាក់ប្រាក់៖ ...")

async def handle_redeem(message: Message):
    await message.answer("វិធីសាស្ត្រក្នុងការប្រើប្រាស់ Redeem Code៖ ...")

async def main():
    if not TOKEN:
        print("Error: TOKEN environment variable not found!")
        return
        
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, CommandStart())
    dp.message.register(handle_account, F.text == "👤 គណនី")
    dp.message.register(handle_products, F.text == "🛍️ ទំនិញ")
    dp.message.register(handle_history, F.text == "🗂️ បញ្ជីទិញសរុប")
    dp.message.register(handle_deposit, F.text == "💰 ដាក់ប្រាក់")
    dp.message.register(handle_redeem, F.text == "⁉️ របៀបប្រើប្រាស់ Redeem Code")

    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
