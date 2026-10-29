from aiogram import Router, types, filters
import datetime
rt = Router()
@rt.message(filters.Command("son"))
async def son(msg: types.Message):
   if msg.pinned_message:
      await msg.answer("xabarni pinga qo'yibaa qoydingiz")
   if msg.reply_to_message:
      await msg.answer("nima bolyabdi brodar")
   if msg.media_group_id:
      await msg.answer("siz menga koproq rasm yubordingiz")
   else:
      await msg.answer("siz menga bita son yoki malumot jonating")
   await msg.answer(str(msg.message_id))
