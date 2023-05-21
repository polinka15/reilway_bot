import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6073566355:AAHX4DAWDb0Xdh6fMyVNKRW7SSa1lJefo88'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply('Start')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply('Вы обратились к справке бота')


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer('Я не работаю в личном диалоге')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
