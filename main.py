import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from random import choice
from aiogram.filters import Command
from aiogram.types import FSInputFile


bot = Bot(token='6615220681:AAHjFJ-cJno14NiUHbU8_b670D5BHxW43SA')
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text)


@dp.message(Command('info'))
async def info(message: types.Message):
    text = (f'Your id is {message.from_user.id}\n'
            f'Your username is {message.from_user.username}\n'
            f'Your fullname is {message.from_user.full_name}\n')
    await message.answer(text=text)


@dp.message(Command('picture'))
async def picture(message: types.Message):
    path = 'media/images.jpeg'
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='beautiful picture')


@dp.message(Command('picture_random'))
async def picture_random(message: types.Message):
    photos = os.listdir('media/')
    path = f'media/{choice(photos)}'
    print(photos)
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='beautiful picture')


@dp.message()
async def echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
