from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("malumotlar"))
async def malumotlar(msg: types.Message):
    await msg.answer("bizdaga barcha malumotlar")
    await msg.answer("botni ochilgan sanasi \n 10.10.2026yilda ocilgan botimiz \n botni egasi  ismi: Ne'matjon familya: Normatov sh botni egasi boladi \n botni egasini yili:2015yilda tavalup topkan \n")
    await msg.answer("botimiz hozurgi vaqtda yangi bir ikkita momolari bor shuning uchun kechiraslar")
    await msg.answer("bizda barcha malumotlar shu edi holos qolgan qismini 23.11.2026 kunda qoshamiz ")