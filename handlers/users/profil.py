from aiogram import Router, types
rt = Router()
@rt.message()
async def profiil(msg: types.Message):
    n = "o'zinggiz haqingizda malumotni oling:\n"
    n += f"id: {msg.chat.id}\n"
    n += f"ismingiz: {msg.chat.first_name}\n"
    n += f"familyangiz: {msg.chat.last_name}\n"
    if msg.chat.username:
        n += f"username: @{msg.chat.username}\n"
    else:
        n += f"username: mavjud emas\n"
    n += f"guruh nomi: {msg.chat.title}\n"
    if msg.chat.type == "private":
        n += f"siz lichkada yozyapsiz"
    else:
        n += f"siz gurpada yazyapsiz"
    await msg.answer(n)
