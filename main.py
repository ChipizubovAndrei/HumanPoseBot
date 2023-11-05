import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

from model import *
from utils import *

TOKEN = ""
SAVE_DIR = './'
PREDICT_DIR = "./"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

@dp.message_handler(content_types=["photo"])
async def photo_handler(message: types.Message):
    image_name = 'user_photo.jpg'
    predicted_image = 'predict_photo.jpg'
    await message.photo[-1].download(destination_file=image_name)

    '''
    TODO
    Предсказания модели
    '''

    await bot.send_photo(message.chat.id, open(image_name, 'rb'))

    clearup_images(SAVE_DIR)
    clearup_images(PREDICT_DIR)

@dp.message_handler(content_types=["document"])
async def photo_handler(message: types.Message):
    await message.reply(f"Отправьте фото, а не документ")

if __name__ == "__main__":
    executor.start_polling(dp)
