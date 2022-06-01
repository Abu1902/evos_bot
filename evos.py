from TOKEN import TOKEN 
import logging
 
from aiogram import Bot, Dispatcher, executor, types
 
from buttons import *

from aiogram.types import Message, CallbackQuery

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("<b>Assalomu aleykum!\nMen mahsulotlaringizni yetkazib beruchi botman </b>",parse_mode='HTML',reply_markup = menu)

@dp.message_handler(text="🚚Buyurtma")
async def uzbecha_uchun(message: types.Message):
    
    await message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=abc)

@dp.message_handler(text="🍽Menu")
async def uzbecha_uchun(message: types.Message):
    
    await message.answer("Ushbu mahsulotlning birini tanglang" ,reply_markup=mena)








###########################################
# MAHSULOT TUR

@dp.callback_query_handler(text="lavash")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/lavashmenu.jpg','rb'),
        caption="""Ushbu mahsulotlning turini tanglang""",reply_markup=lavashmenu)
    await call.message.delete()


@dp.callback_query_handler(text="shaurma")
async def menu_uchun(call: CallbackQuery):
 
     await call.message.answer_photo(
      photo=open('rasmlar/shaurmamenu.jpg','rb'),
      caption=""""Ushbu mahsulotlning turini tanglang""",reply_markup=shaurmamenu)
     await call.message.delete()

@dp.callback_query_handler(text="burger")
async def menu_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
      photo=open('rasmlar/burger.jpg','rb'),

      caption=""""Ushbu mahsulotlning turini tanglang""",reply_markup=burgermenu)
    await call.message.delete()

@dp.callback_query_handler(text="hotdog")
async def menu_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=hotdogmenu)


@dp.callback_query_handler(text="sendvich")
async def menu_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
      photo=open('rasmlar/sendvich.jpg','rb'),

      caption=""""Ushbu mahsulotlning turini tanglang""",reply_markup=senvichmenu)

    await call.message.delete()
@dp.callback_query_handler(text="donar")
async def menu_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=donarmenu)


@dp.callback_query_handler(text="gazaklar")
async def menu_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=gazaklarmenu)

@dp.callback_query_handler(text="ichimlik")
async def menu_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=ichimlik_menyu1)

@dp.callback_query_handler(text="desert")
async def menu_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
      photo=open('rasmlar/desert.jpg','rb'),
      caption="""Ushbu mahsulotlning turini tanglang""",reply_markup=desertmenu)
    await call.message.delete()

@dp.callback_query_handler(text="pitsa")
async def menu_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=pizzamenu)



###########################################


# Lavash
##########################################
@dp.callback_query_handler(text="gusht")
async def lavashmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglangg",reply_markup=lavashmenuturigusht)

@dp.callback_query_handler(text="tovuq")
async def lavashmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=lavashmenuturitovuq)

@dp.callback_query_handler(text="gusht pishloqli")
async def lavashmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=lavashmenuturigushtpishloqli)

@dp.callback_query_handler(text="tovuq pishloqli")
async def lavashmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=lavashmenuturitovuqpishloqli)



##########################################
@dp.callback_query_handler(text="mini1")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
        photo=open('rasmlar/lavash1.jpg','rb'),
        caption="""Narxi:   21 000 so'm\nTarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting""",reply_markup=son1)
    await call.message.delete()
@dp.callback_query_handler(text="classic1")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
        photo=open('rasmlar/lavash1.jpg','rb'),
        caption="""Narxi:   24 000 so'm \nTarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting""",reply_markup=son1)
    await call.message.delete()

@dp.callback_query_handler(text="mini2")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
     await call.message.answer_photo(
        photo=open('rasmlar/lavashtovuq.jpg','rb'),
        caption="""Narxi:   19 000 so'm\nTarkibi: Xamir, Tovuq  go`sht, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting""",reply_markup=son2)
     await call.message.delete()

@dp.callback_query_handler(text="classic2")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
     await call.message.answer_photo(
        photo=open('rasmlar/lavashtovuq.jpg','rb'),
        caption="""21 000 so'm\nTarkibi: Xamir, Tovuq  go`sht, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting""",reply_markup=son2)
     await call.message.delete()
@dp.callback_query_handler(text="mini3")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
     await call.message.answer_photo(
        photo=open('rasmlar/lavashpishloqli.jpg','rb'),
        caption="""Narxi:   21 000 so'm\nTarkibi: Xamir, Tovuq  go`sht, chips, pomidor, bodring, sous, mayonez,pishloq \nMiqdorini tanlang yoki kiriting""",reply_markup=son3)
     await call.message.delete()
@dp.callback_query_handler(text="classic3")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
      await call.message.answer_photo(
        photo=open('rasmlar/lavashpishloqli.jpg','rb'),
        caption="""23 000 so'm\nTarkibi: Xamir, Tovuq  go`sht, chips, pomidor, bodring, sous, mayonez,pishloq \nMiqdorini tanlang yoki kiriting""",reply_markup=son3)
      await call.message.delete()

@dp.callback_query_handler(text="mini4")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
      await call.message.answer_photo(
        photo=open('rasmlar/lavashpishloqli2.jpg','rb'),
        caption="""Narxi:   23 000 so'm \nTarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez,pishloq \nMiqdorini tanlang yoki kiriting""",reply_markup=son4)
      await call.message.delete()

@dp.callback_query_handler(text="classic4")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
      await call.message.answer_photo(
        photo=open('rasmlar/lavashpishloqli2.jpg','rb'),
        caption="""Narxi:   25 000 so'm \nTarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez,pishloq \nMiqdorini tanlang yoki kiriting""",reply_markup=son4)
      await call.message.delete()
##########################################






# BACKLAR
############################################
@dp.callback_query_handler(text="back1")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=abc)

@dp.callback_query_handler(text="back2")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)


@dp.callback_query_handler(text="back3")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=lavashmenu)


@dp.callback_query_handler(text="back4")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=lavashmenuturigusht)

@dp.callback_query_handler(text="back5")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=lavashmenuturitovuq)



@dp.callback_query_handler(text="back6")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=lavashmenuturitovuqpishloqli)

@dp.callback_query_handler(text="back7")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=lavashmenuturigushtpishloqli)

@dp.callback_query_handler(text="back8")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back15")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=shaurmamenu)
@dp.callback_query_handler(text="back9")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=lavashmenu)


@dp.callback_query_handler(text="back10")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=shaurmamenuturigusht)

@dp.callback_query_handler(text="back11")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=shaurmamenuturitovuq)



@dp.callback_query_handler(text="back12")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=shaurmamenuturigushtqalampir )

@dp.callback_query_handler(text="back13")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni turini tanglang </b>",parse_mode='HTML',reply_markup=shaurmamenuturitovuqqalampir)

@dp.callback_query_handler(text="back14")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back16")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=burgermenu)


@dp.callback_query_handler(text="back17")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=burgermenuturioddiy)


@dp.callback_query_handler(text="back18")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=burgermenuturicheese)

@dp.callback_query_handler(text="back19")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back20")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=hotdogmenu)

@dp.callback_query_handler(text="back21")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=hotdogmenu)

@dp.callback_query_handler(text="back22")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=hotdogmenu)

@dp.callback_query_handler(text="back23")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=hotdogmenu)

@dp.callback_query_handler(text="back24")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back25")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=senvichmenu)

@dp.callback_query_handler(text="back26")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=senvichmenu)

@dp.callback_query_handler(text="back27")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back28")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=donarmenu)

@dp.callback_query_handler(text="back29")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=donarmenu)

@dp.callback_query_handler(text="back30")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back31")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=gazaklarmenu)

@dp.callback_query_handler(text="back32")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=gazaklarmenu)

@dp.callback_query_handler(text="back33")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=gazaklarmenu)

@dp.callback_query_handler(text="back34")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=gazaklarmenu)

@dp.callback_query_handler(text="back35")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)


@dp.callback_query_handler(text="back36")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=desertmenu)

@dp.callback_query_handler(text="back37")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=desertmenu)


@dp.callback_query_handler(text="back38")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=desertmenu)

@dp.callback_query_handler(text="back39")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)

@dp.callback_query_handler(text="back40")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=pizzamenu)

@dp.callback_query_handler(text="back41")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=pizzamenu)

@dp.callback_query_handler(text="back42")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=pizzamenu)


@dp.callback_query_handler(text="back49")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu3)

@dp.callback_query_handler(text="back50")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu3)

@dp.callback_query_handler(text="back51")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu3)

@dp.callback_query_handler(text="back52")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu3)

@dp.callback_query_handler(text="back53")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu4)

@dp.callback_query_handler(text="back54")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu4)

@dp.callback_query_handler(text="back55")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu4)

@dp.callback_query_handler(text="back56")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=pizzamenu)

@dp.callback_query_handler(text="back48")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlik_menyu1)



@dp.callback_query_handler(text="back57")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlikmenuturiyaxna)


@dp.callback_query_handler(text="back58")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlikmenuturiyaxna)

@dp.callback_query_handler(text="back59")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlikmenuturiyaxna)


@dp.callback_query_handler(text="back60")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichimlikmenuturiyaxna)


@dp.callback_query_handler(text="back61")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichmlikmenuturifresh)



@dp.callback_query_handler(text="back62")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=ichmlikmenuturifresh)


@dp.callback_query_handler(text="orqaga20")
async def ortga(call: CallbackQuery):
 await call.message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=mena)























@dp.message_handler(text="◀️ortga")
async def uzbecha_uchun(message: types.Message):
 
 await message.answer("<b> Mahsulotlarni tanglang </b>",parse_mode='HTML',reply_markup=menu)



############################################




# Shaurma
#################################################

@dp.callback_query_handler(text="gusht1")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
    await call.message.answer("Ushbu mahsulotlning turini tanglangg",reply_markup=shaurmamenuturigusht)
  

@dp.callback_query_handler(text="tovuq1")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
    await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=shaurmamenuturitovuq)

@dp.callback_query_handler(text="gushtqalampir")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
    await call.message.answer(" Ushbu mahsulotlning turini tanglang",reply_markup=shaurmamenuturigushtqalampir)

@dp.callback_query_handler(text="tovuqqalampir")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
    await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=shaurmamenuturitovuqqalampir)

##########################################


#################################################


@dp.callback_query_handler(text="mini5")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurmagusht.jpg','rb'),
        caption="""Narxi:   18 000 so'm\nTarkibi: Kulcha, go'sht, pomidor, sous,  piyoz.  \nMiqdorini tanlang yoki kiriting""",reply_markup=son5)
 await call.message.delete()


@dp.callback_query_handler(text="classic5")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
  await call.message.answer_photo(
        photo=open('rasmlar/shaurmagusht.jpg','rb'),
        caption="""Narxi:   20 000 so'm \nTarkibi: Kulcha, go'sht, pomidor, sous,  piyoz. \nMiqdorini tanlang yoki kiriting""",reply_markup=son5)
  await call.message.delete()

@dp.callback_query_handler(text="mini6")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurmatovuq.jpg','rb'),
        caption="""Narxi:   20 000 so'm\nTarkibi: Kulcha,tovuq go'shti, pomidor, sous,  piyoz. \nMiqdorini tanlang yoki kiriting""",reply_markup=son6)
 await call.message.delete()

@dp.callback_query_handler(text="classic6")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
  await call.message.answer_photo(
        photo=open('rasmlar/shaurmatovuq.jpg','rb'),
        caption="""22 000 so'm\nTarkibi:Kulcha,tovuq go'shti, pomidor, sous,  piyoz. \nMiqdorini tanlang yoki kiriting""",reply_markup=son6)
  await call.message.delete()

@dp.callback_query_handler(text="mini7")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurma3.jpg','rb'),
        caption="""Narxi:   21 000 so'm\nTarkibi: Kulcha, go'sht, pomidor, achiq sous,  piyoz,. \nMiqdorini tanlang yoki kiriting""",reply_markup=son7)
 await call.message.delete()

@dp.callback_query_handler(text="classic7")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurma3.jpg','rb'),
        caption="""23 000 so'm\nTarkibi: Kulcha, go'sht, pomidor, achiq sous,  piyoz, \nMiqdorini tanlang yoki kiriting""",reply_markup=son7)

 await call.message.delete()

@dp.callback_query_handler(text="mini8")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurma4.jpg','rb'),
        caption="""Narxi:   20 000 so'm \nTarkibi: Kulcha,tovuq go'shti, pomidor,achiq sous,  piyoz. \nMiqdorini tanlang yoki kiriting""",reply_markup=son8)
 await call.message.delete()

@dp.callback_query_handler(text="classic8")
async def shaurmamenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/shaurma4.jpg','rb'),
        caption="Narxi:   22 000 so'm \nTarkibi: Kulcha,tovuq go'shti, pomidor, achiq sous,  piyoz. mayonez,pishloq \nMiqdorini tanlang yoki kiriting",reply_markup=son8)
 await call.message.delete()
##########################################

# BURGER

@dp.callback_query_handler(text="gamburger")
async def gamburgermenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglangg",reply_markup=burgermenuturioddiy)

@dp.callback_query_handler(text="chiz")
async def gamburgermenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=burgermenuturicheese)


@dp.callback_query_handler(text="classic9")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/burger1.jpg','rb'),
        caption="""Narxi:   20 000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son9)
 await call.message.delete()

@dp.callback_query_handler(text="big1")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/burger4.jpg','rb'),
        caption="""Narxi:   24 000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son9)
 await call.message.delete()

@dp.callback_query_handler(text="classic10")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/burger2.jpg','rb'),
        caption="""Narxi:   22000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son10)
 await call.message.delete()

@dp.callback_query_handler(text="big2")
async def lavashmenusoni_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/burger3.jpg','rb'),
        caption="""Narxi:   24 000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son10)
 await call.message.delete()

# Hot-Dog

@dp.callback_query_handler(text="dabl")
async def hotdogmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/hot1.jpg','rb'),
        caption="""Narxi:    18000 ming so'm\nTarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\nMiqdorini tanlang yoki kiriting""",reply_markup=son11)
 await call.message.delete()

@dp.callback_query_handler(text="classic11")
async def hotdogmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/hot2.jpg','rb'),
        caption="""Narxi:    8000 so'm\nTarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.\nMiqdorini tanlang yoki kiriting""",reply_markup=son12)
 await call.message.delete()

@dp.callback_query_handler(text="korol")
async def hotdogmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/hot3.jpg','rb'),
        caption="""Narxi:    15000 so'm\nTarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.\nMiqdorini tanlang yoki kiriting""",reply_markup=son13)
 await call.message.delete()

@dp.callback_query_handler(text="tovuq2")
async def hotdogmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/hot4.jpg','rb'),
        caption="""Narxi:    17000 so'm\nTarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.\nMiqdorini tanlang yoki kiriting""",reply_markup=son14)
 await call.message.delete()

# Sendvich


@dp.callback_query_handler(text="classic12")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/sendvich3.jpg','rb'),caption="""Narxi:    22000 ming so'm\nTarkibi:✅Kulcha, go'sht, pomidor, sous,  piyoz..\nMiqdorini tanlang yoki kiriting""",reply_markup=son15)
 await call.message.delete()
@dp.callback_query_handler(text="tovuq3")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/sendvich3.jpg','rb'),caption="""Narxi:    20000 so'm\nTarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz..\nMiqdorini tanlang yoki kiriting""",reply_markup=son16)
 await call.message.delete()
# Donar

@dp.callback_query_handler(text="gusht2")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/donar1.jpg','rb'),
        caption="""Narxi:    23000 ming so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son17)
 await call.message.delete()

@dp.callback_query_handler(text="tovuq4")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
  await call.message.answer_photo(
        photo=open('rasmlar/donar2.jpg','rb'),
        caption="""Narxi:    21000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son18)
  await call.message.delete()
# Gazaklar

@dp.callback_query_handler(text="fri")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/fri.jpg','rb'),
        caption="""Narxi:    6000 ming so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son19)
 await call.message.delete()

@dp.callback_query_handler(text="derevenskiy")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/kartoshka.jpg','rb'),
        caption="""Narxi:    8000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son20)
 await call.message.delete()

@dp.callback_query_handler(text="guruchkatta")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/guruch.jpg','rb'),
        caption="""Narxi:    10000 ming so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son21)
 await call.message.delete()

@dp.callback_query_handler(text="guruchkichik")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/guruch.jpg','rb'),
        caption="""Narxi:    8000 so'm\nMiqdorini tanlang yoki kiriting""",reply_markup=son22)
 await call.message.delete()
# Ichimlik

@dp.callback_query_handler(text="choykofe")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="kofe")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)


@dp.callback_query_handler(text="americano")
async def suv(call:CallbackQuery):
   await call.message.answer_photo(
        photo=open('rasmlar/kofe.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik americano\nNarxi:5000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)
   await call.message.delete()

@dp.callback_query_handler(text="capuchino")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/kofe.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik capuchino\nNarxi:7000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)

    await call.message.delete()

@dp.callback_query_handler(text="3v1")
async def suv(call:CallbackQuery):
   await call.message.answer_photo(
        photo=open('rasmlar/kofe.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik 3v1 cofe\nNarxi:4000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)

   

@dp.callback_query_handler(text="latte")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/kofe.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik latte\nNarxi:8000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)

    await call.message.delete()

@dp.callback_query_handler(text="choylar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="kuk")
async def suv(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('rasmlar/choy.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik kuk choy\nNarxi:2000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)
     await call.message.delete()

@dp.callback_query_handler(text="qora")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/choy.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik qora choy\nNarxi:2000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)

    await call.message.delete()

@dp.callback_query_handler(text="limon")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/choy.jpg','rb'),caption="""<b>Hurmatli mijoz\nsiz tanlagan ichimlik limon choy\nNarxi:3000 \nltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="orqaga5")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="orqaga6")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga7")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga10")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)

@dp.callback_query_handler(text="orqaga13")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga11")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga8")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)


@dp.callback_query_handler(text="orqaga12")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga9")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga14")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)



@dp.callback_query_handler(text="fanta")
async def suv(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open('rasmlar/fanta.jpg','rb'),caption="""<b>Narxi:    11000 so'm</b>""",parse_mode = 'HTML',reply_markup = son30)
     await call.message.delete()


@dp.callback_query_handler(text="cola")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/cola.jpg','rb'),caption="""<b>Narxi:    11000 so'm</b>""",parse_mode = 'HTML',reply_markup = son31)
    await call.message.delete()

@dp.callback_query_handler(text="sprite")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/sprite.jpg','rb'),caption="""<b>Narxi:    11000 so'm</b>""",parse_mode = 'HTML',reply_markup = son32)
    await call.message.delete()

@dp.callback_query_handler(text="nestle")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/nestle.jpg','rb'),caption="""<b>Narxi:    6000 so'm</b>""",parse_mode = 'HTML',reply_markup = son33)
    await call.message.delete()

@dp.callback_query_handler(text="bliss")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/bliss.jpg','rb'),caption="""<b>Narxi:    12000 so'm</b>""",parse_mode = 'HTML',reply_markup = son34)
    await call.message.delete()

@dp.callback_query_handler(text="olmasabzi")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/sok.jpg','rb'),caption="""<b>Narxi:    15000 so'm</b>""",parse_mode = 'HTML',reply_markup = son35)

   
    await call.message.delete()    






@dp.callback_query_handler(text="yaxna")
async def ichimlikmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=ichimlikmenuturiyaxna)

@dp.callback_query_handler(text="fresh")
async def ichimlikmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer("Ushbu mahsulotlning turini tanglang",reply_markup=ichmlikmenuturifresh)
#######################



#DESERTLAR
@dp.callback_query_handler(text="asal")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/asal.jpg','rb'),caption="""Narxi:    14000 ming so'm\n✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem\nMiqdorini tanlang yoki kiriting""",reply_markup=son23)
 await call.message.delete()  

@dp.callback_query_handler(text="qulupnay")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/qulupnay.jpg','rb'),caption="""Narxi:    14000 so'm\n✅Qulupnayli Muss.\nMiqdorini tanlang yoki kiriting""",reply_markup=son24)

 await call.message.delete()  

@dp.callback_query_handler(text="choco")
async def sendvichmenuturi_uchun(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open('rasmlar/choco.jpg','rb'),caption="""Narxi:    14000 ming so'm\n✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.\nMiqdorini tanlang yoki kiriting""",reply_markup=son25)
    await call.message.delete()  

# Pizza

@dp.callback_query_handler(text="pizza1")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
    await call.message.answer_photo(
        photo=open('rasmlar/peperoni.jpg','rb'),caption="""Narxi:    65000 ming so'm\n✅Пицца Пепперони\nПицца Пепперони     33см.\nСоус Томатный Для Пиццы\nТонкое тесто.\nСыр 110 гр.\nMiqdorini tanlang yoki kiriting""",reply_markup=son26)
    await call.message.delete()  

@dp.callback_query_handler(text="pizza2")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/ana.jpg','rb'),caption="""Narxi:    65000 so'm\n✅Пицца с Ананасом.\nПицца с Колбасой     33см..\nСоус Томатный Для Пиццы\nТонкое тесто.\nСыр 110 гр.\n3 вида колбас 130гр.\nГрибы\nMiqdorini tanlang yoki kiriting""",reply_markup=son27)
 await call.message.delete()  


@dp.callback_query_handler(text="pizza3")
async def sendvichmenuturi_uchun(call: CallbackQuery):
 
 await call.message.answer_photo(
        photo=open('rasmlar/margarita.jpg','rb'),caption="""Narxi:    14000 ming so'm\n✅Пицца Маргарита\nПицца Маргарита  33см.\nСоус Томатный Для Пиццы \nТонкое тесто \nСыр 100гр.\nПомидоры\nMiqdorini tanlang yoki kiriting""",reply_markup=son28)
 await call.message.delete()  



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)