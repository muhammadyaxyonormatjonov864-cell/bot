from aiogram import Router, types, F
rt = Router()
@rt.message(F.video)
async def video(msg: types.Message):
   await msg.answer("siz uzunvaqtli video yoki qisqa video yubordingiz")

