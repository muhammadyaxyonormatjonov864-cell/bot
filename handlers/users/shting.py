from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("emoji"))
async def emoji(msg: types.Message):

    await msg.answer_dice(emoji="🎲")
    await msg.answer("mana emoji sizga")