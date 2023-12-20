import asyncio
import time
import logging
import os
import shutil

from aiogram import Bot, Dispatcher, executor, types
from model import poseEstimator

TOKEN = ""
MODEL_PATH = 'models/yolov8n-pose.pt'
SAVE_DIR = './tmp'

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
    user_id = str(message.from_user.id)
    user_save_dir = os.path.join(SAVE_DIR, user_id)
    os.mkdir(user_save_dir)
    image_name = os.path.join(user_save_dir, 'image.jpg')
    predicted_image = os.path.join(user_save_dir, 'predict', 'image.jpg')
    await message.photo[-1].download(destination_file=image_name)

    results = poseEstimator(image_name, project=user_save_dir, save=True)

    await bot.send_photo(message.chat.id, open(predicted_image, 'rb'))

    shutil.rmtree(user_save_dir)

@dp.message_handler(content_types=["document"])
async def photo_handler(message: types.Message):
    await message.reply(f"Отправьте фото, а не документ")

if __name__ == "__main__":
    if not os.path.exists(SAVE_DIR):
        os.mkdir(SAVE_DIR)

    executor.start_polling(dp)
