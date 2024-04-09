from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keys(button1_teg, button2_teg=""):
    if button2_teg != "":
        result = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='📖 ТЕКСТ', callback_data=button1_teg),
            InlineKeyboardButton(text='📺 ВИДЕО', callback_data=button2_teg)
        ]])
    else:
        result = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='⬇️ ДАЛЕЕ', callback_data=button1_teg)
        ]])

    return result


les_0 = keys("lesson0_article", "lesson0_video")
les_video_0 = keys("lesson1")

les_1 = keys("lesson1_article", "lesson1_video")
les_video_1 = keys("lesson2")

les_2 = keys("lesson2_article", "lesson2_video")
les_video_2 = keys("lesson3")

les_3 = keys("lesson3_article", "lesson3_video")
les_video_3 = keys("lesson4")

les_4 = keys("lesson4_article", "lesson4_video")
les_video_4 = keys("lesson5")

les_5 = keys("lesson5_article", "lesson5_video")
les_video_5 = keys("lesson6")

les_6 = keys("lesson6_article", "lesson6_video")
les_video_6 = keys("lesson7")

les_7 = keys("lesson7_article", "lesson7_video")
les_video_7 = keys("lesson8")

les_8 = keys("lesson8_article", "lesson8_video")
les_video_8 = keys("lesson9")

les_9 = keys("lesson9_article", "lesson9_video")
