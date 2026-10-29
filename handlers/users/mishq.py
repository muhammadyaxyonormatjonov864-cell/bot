from aiogram import Router, types, filters, F
import random

rt = Router()

@rt.message(filters.Command("mushuk"))
@rt.message(F.text.lower() == "mushuk")
async def mushuk(msg: types.Message):
    rasmlar = [
        "https://i.pinimg.com/236x/1b/40/3e/1b403e1d36856d81f9b74fd37c6eabe1.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRV9Dap_7H8C49Kdp8oTAJgDlk1Rz92Qylsi0RkpQ-nMA&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRewknZRoB109AIxyuMjCpUf5lhSXW0kKB9Il-cvay4ZF3TGWQG_mKNif8&s=10 \n mushuk dedingiz mama mushuk",

    ]
    await msg.answer("yana ti yoki mushukdesangiz random tzrizda ishlaydi")
    rasm = random.choice(rasmlar)
    await msg.answer_photo(rasm)