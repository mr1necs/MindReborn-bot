from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command

import app.textboxs as text
import app.keyboards as kb
from app.links import image, video
from app.parser import worksheet
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class GetPhone(StatesGroup):
    phone = State()


# ############################################### LESSON 0 ############################################### #
@router.message(Command('start'))
async def share_number(message: Message, state: FSMContext):
    await message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=kb.contact_keyboard())
    await state.set_state(GetPhone.phone)


@router.message(GetPhone.phone)
async def get_contact(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    await message.answer("Спасибо", reply_markup=ReplyKeyboardRemove())
    await state.clear()
    worksheet.insert_row([str(message.from_user.id), contact], 2)

    welcome_text = str(text.TEXT_LESSON_0_1) + str(message.from_user.full_name) + str(text.TEXT_LESSON_0_2)
    await message.answer_photo(photo=image[0], caption=welcome_text,
                               parse_mode='HTML', reply_markup=kb.les_0)


@router.callback_query(F.data == "lesson0_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[0], caption="", reply_markup=kb.les_video_0)


# ############################################### LESSON 1 ############################################### #
@router.callback_query(F.data == "lesson1")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[1], caption=text.TEXT_LESSON_1,
                                        parse_mode='HTML', reply_markup=kb.les_1)


@router.callback_query(F.data == "lesson1_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[1], caption="", reply_markup=kb.les_video_1)


# ############################################### LESSON 2 ############################################### #
@router.callback_query(F.data == "lesson2")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[2], caption=text.TEXT_LESSON_2,
                                        parse_mode='HTML', reply_markup=kb.les_2)


@router.callback_query(F.data == "lesson2_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[2], caption="", reply_markup=kb.les_video_2)


# ############################################### LESSON 3 ############################################### #
@router.callback_query(F.data == "lesson3")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[3], caption=text.TEXT_LESSON_3,
                                        parse_mode='HTML', reply_markup=kb.les_3)


@router.callback_query(F.data == "lesson3_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[3], caption="", reply_markup=kb.les_video_3)


# ############################################### LESSON 4 ############################################### #
@router.callback_query(F.data == "lesson4")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[4], caption=text.TEXT_LESSON_4,
                                        parse_mode='HTML', reply_markup=kb.les_4)


@router.callback_query(F.data == "lesson4_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[4], caption="", reply_markup=kb.les_video_4)


# ############################################### LESSON 5 ############################################### #
@router.callback_query(F.data == "lesson5")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[5], caption=text.TEXT_LESSON_5,
                                        parse_mode='HTML', reply_markup=kb.les_5)


@router.callback_query(F.data == "lesson5_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[5], caption="", reply_markup=kb.les_video_5)


# ############################################### LESSON 6 ############################################### #
@router.callback_query(F.data == "lesson6")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[6], caption=text.TEXT_LESSON_6,
                                        parse_mode='HTML', reply_markup=kb.les_6)


@router.callback_query(F.data == "lesson6_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[6], caption="", reply_markup=kb.les_video_6)


# ############################################### LESSON 7 ############################################### #
@router.callback_query(F.data == "lesson7")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[7], caption=text.TEXT_LESSON_7,
                                        parse_mode='HTML', reply_markup=kb.les_7)


@router.callback_query(F.data == "lesson7_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[7], caption="", reply_markup=kb.les_video_7)


# ############################################### LESSON 8 ############################################### #
@router.callback_query(F.data == "lesson8")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[8], caption=text.TEXT_LESSON_8,
                                        parse_mode='HTML', reply_markup=kb.les_8)


@router.callback_query(F.data == "lesson8_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[8], caption="", reply_markup=kb.les_video_8)


# ############################################### LESSON 9 ############################################### #
@router.callback_query(F.data == "lesson9")
async def lesson(callback: CallbackQuery):
    await callback.message.answer_photo(photo=image[9], caption=text.TEXT_LESSON_9,
                                        parse_mode='HTML', reply_markup=kb.les_9)


@router.callback_query(F.data == "lesson9_video")
async def video_lesson(callback: CallbackQuery):
    await callback.message.answer_video(video=video[9], caption="")

