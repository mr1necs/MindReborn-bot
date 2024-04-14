from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from app.links import article


def contact_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер телефона 📱", request_contact=True)]],
                                   resize_keyboard=True)
    return keyboard


def keys(button_teg, button_url=""):
    if button_url != "":
        result = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='📖 ТЕКСТ', url=button_url),
            InlineKeyboardButton(text='📺 ВИДЕО', callback_data=button_teg)
        ]])
    else:
        result = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='⬇️ ДАЛЕЕ', callback_data=button_teg)
        ]])

    return result


les_0 = keys("lesson0_video", article[0])
les_video_0 = keys("lesson1")

les_1 = keys("lesson1_video", article[1])
les_video_1 = keys("lesson2")

les_2 = keys("lesson2_video", article[2])
les_video_2 = keys("lesson3")

les_3 = keys("lesson3_video", article[3])
les_video_3 = keys("lesson4")

les_4 = keys("lesson4_video", article[4])
les_video_4 = keys("lesson5")

les_5 = keys("lesson5_video", article[5])
les_video_5 = keys("lesson6")

les_6 = keys("lesson6_video", article[6])
les_video_6 = keys("lesson7")

les_7 = keys("lesson7_video", article[7])
les_video_7 = keys("lesson8")

les_8 = keys("lesson8_video", article[8])
les_video_8 = keys("lesson9")

les_9 = keys("lesson9_video", article[9])
