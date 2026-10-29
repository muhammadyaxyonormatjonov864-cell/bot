from aiogram import Router, types, F
rt = Router()
@rt.message(F.txt)
async def txt(msg: types.Message):
   await msg.answer("siz txt tashadingiz")
