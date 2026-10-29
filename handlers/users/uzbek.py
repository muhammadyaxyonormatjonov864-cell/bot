from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("prizdent"))
async def prizdent(msg: types.Message):
    await msg.answer_photo("https://president.uz/img/president_img.jpg", caption="uzb prizdent rasmi ")
