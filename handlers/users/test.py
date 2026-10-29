from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def test(msg: types.Message):
    print(msg.from_user.id)


