from aiogram import Router, types, filters, F
import random

rt = Router()

@rt.message(filters.Command("it"))
@rt.message(F.text.lower() == "it")
async def it(msg: types.Message):
    rasmlar = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVRbDh1qocYa0Sl4HwmyZ9R9zCu10nruzqQ-SQrhYFDqZ_r8qs1rSHq0w&s=10 \n mana it",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRV_E-3vOgaDNfyya2gG8CJdL_vtaFOMfpBWIAqzQSCFg&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMARPsbfJoOnXPFYZL42HyTBZM1aDBOgelg5HiXH7IJQ&s \n mana it dedingiz itni rasmini tashadim",
    ]
    await msg.answer("yana ti yoki mushukdesangiz random tzrizda ishlaydi")
    rasm = random.choice(rasmlar)
    await msg.answer_photo(rasm)