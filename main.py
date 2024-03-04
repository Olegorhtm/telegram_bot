import asyncio
import csv
import time
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.client import bot
from aiogram.types import URLInputFile
from aiogram.utils.markdown import hbold, hlink, hunderline, hstrikethrough
from aiogram.filters.command import Command

bot = Bot('6411865082:AAEdgVUzGwGjrkEsHQUDE1W3J6duza8k7nc', parse_mode="HTML")
chanel_name = '@pumaNoOfficial'
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


async def main():
    await dp.start_polling(bot, skip_updates=True)


@dp.message(Command("start"))
async def buttons(message: types.Message):
    start_buttons = [[types.KeyboardButton(text="Все_продукты")], [types.KeyboardButton(text="Скидки")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

    await message.answer("Продукты Puma", reply_markup=keyboard)


@dp.message(F.text.lower() == "все_продукты")
async def poster(message: types.Message):
    with (open("product.csv", encoding='utf8') as read_file):
        file_reader = csv.DictReader(read_file, delimiter=",")
        for row in file_reader:
            product = f"{hlink(row['name'], row['link'])} \n\n" \
                      f"Description: {hbold(row['description'])}\n\n" \
                      f"Price: {hstrikethrough(row['price'])}\n\n" \
                      f"Sale: {hunderline(row['sale'])}\n\n"

            image = URLInputFile(row['photo'])
            time.sleep(3)
            await bot.send_message(chat_id=chanel_name, text=product)


@dp.message(F.text.lower() == "cкидки")
async def poster(message: types.Message):
    with open("pumascrap/pumascrap/spiders/sale.csv", encoding='utf8') as read_file:
        file_reader = csv.DictReader(read_file, delimiter=",")
        for row in file_reader:
            sali = f"Поспешите! Скидка! {row['sale-procent']}\n\n" \
                   f"You code: {row['code-sale']}"
        await bot.send_message(chat_id=chanel_name, text=sali)


if __name__ == '__main__':
    asyncio.run(main())

#    with open("rewrite_product.csv", 'w', newline='') as read_dict:
#                 new_dict = csv.DictWriter(read_dict, fieldnames=file_reader)
#                 for new_row in new_dict:
#                      if new_row['link'] != row['link']:
#                         # write = csv.writer(new_dict)
#                         new_dict.writerows(new_row[product, image])
#                          if
#                     else:
#                         break
