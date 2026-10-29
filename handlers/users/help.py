from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman?")
    n = "bizning barcha kamandalarimiz:\n"
    n += "/soat\n"
    n += "/sana\n"
    n += "/son\n"
    n += "/it\n"
    n += "/rasm\n"
    n += "/mshshuks\n"
    n += "/emoji\n"
    n += "/admin"
    n += "/profiil\n"
    n += "/prizdent\n"
    await msg.answer(n)
