from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID: {message.photo[-1].file_id}')


@router.message(F.video)
async def get_video(message: Message):
    await message.answer(f'ID: {message.video.file_id}')