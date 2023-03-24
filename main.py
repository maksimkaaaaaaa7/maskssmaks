import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6136648005:AAFooV0cjt3JXi8DrJ08hHvVrWIY0btdRao'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["pn"])
async def send_welcome(message: types.Message):
    await message.reply("Понедельник: начало в 10:30\n\n-\n\n-\n\nКомпьютерные сети: 204\n\nКомпьютерные сети: 204\n\nОсновы электроники: 202\n\nОсновы электроники: 202\n\nООП программирование: 201\n\nООП программирование: 201")

@dp.message_handler(commands=["vt"])
async def send_welcome(message: types.Message):
    await message.reply("Вторник: начало в 12:00\n\n-\n\n-\n\n-\n\n-\n\nФизика: 305\n\nФизика: 305\n\nВысшая математика: 305\n\nВысшая математика: 305\n\nФизическое воспитание: 2 этаж\n\nФизическое воспитание: 2 этаж")

@dp.message_handler(commands=["sr"])
async def send_welcome(message: types.Message):
    await message.reply("Среда: начало в 9:30\n\n-\n\nВоспитательный час\n\nАнглийский: 412\n\nАнглийский: 412\n\nФизика: 305\n\nФизика: 305\n\nВеб технология: 201\n\nВеб технология: 201")

@dp.message_handler(commands=["ct"])
async def send_welcome(message: types.Message):
    await message.reply("Четверг: начало в 9:00\n\nВеб технология: 201\n\nВеб технология: 201\n\nВысшая математика: 305\n\nВысшая математика: 305\n\nУ.П Веб технология: 201\n\nУ.П Веб технология: 201\n\nУ.П Веб технология: 201\n\nУ.П Веб технология: 201")

@dp.message_handler(commands=["pt"])
async def send_welcome(message: types.Message):
    await message.reply("Пятница: начало в 10:30\n\n-\n\n-\n\nИнтернет технология: 201\n\nИнтернет технология: 201\n\nОсновы алгоритмизации: 201\n\nОсновы алгоритмизации: 201\n\nАнглийский: 412\n\nАнглийский: 412\n\nФизическое воспитание: 2 этаж\n\nФизическое воспитание: 2 этаж")

@dp.message_handler(commands=["sb"])
async def send_welcome(message: types.Message):
    await message.reply("Суббота: начало в 9:00\n\nУ.П. Интернет технология: 207\n\nУ.П. Интернет технология: 207\n\nОсновы электроники: 202\n\nОсновы электроники: 202\n\nООП программирование: 201\n\nООП программирование: 201\n\nИнтернет технология: 201\n\nИнтернет технология: 201")

@dp.message_handler(lambda message: message.text.startswith('@chatgptchat14tire2_bot'))
async def handle_message(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.reply(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
