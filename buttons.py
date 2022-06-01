from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

menu = ReplyKeyboardMarkup(
	keyboard=[

		 [
		 KeyboardButton(text="🚚Buyurtma")
		 ],
   		 
	

   		    ],
   		    resize_keyboard=True

	)



mena = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text='🌯Lavash',callback_data='lavash'),
	
	 InlineKeyboardButton(text='🌮Shaurma',callback_data='shaurma')

	],

	[
	 InlineKeyboardButton(text='🍔Burger',callback_data='burger'),
	
	 InlineKeyboardButton(text='🌭Hot-Dog',callback_data='hotdog'),
	

	],

	[
	 InlineKeyboardButton(text='🥪Sendvich club',callback_data='sendvich'),
	
	 InlineKeyboardButton(text='🍱Donar',callback_data='donar'),
	],

	[
	 InlineKeyboardButton(text='🍟Gazaklar',callback_data='gazaklar'),
	
	 InlineKeyboardButton(text='🥤Ichimliklar',callback_data='ichimlik'),
	],

	[
	 InlineKeyboardButton(text='🍰Desertlar',callback_data='desert'),
	
	 InlineKeyboardButton(text='🍕Pizza',callback_data='pitsa'),
	],



	[ InlineKeyboardButton(text='◀️Ortga',callback_data='back1')


	],

	]
	)




  

abc = ReplyKeyboardMarkup(
	keyboard=[

		 [
		 KeyboardButton(text="🍽Menu ")
		 ],
   		 

		
		
   		 
	

   		    ],
   		    resize_keyboard=True



	)





lavashmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🥩Go'shtli lavash",callback_data="gusht"),

	InlineKeyboardButton(text="🍖Tovuqli lavash",callback_data="tovuq"),
	],
[ InlineKeyboardButton(text="🥩Go'shtli lavash pishloqli",callback_data="gusht pishloqli"),

	InlineKeyboardButton(text="🍖Tovuqli lavash pishloqli",callback_data="tovuq pishloqli"),
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back2')


],
],
)


lavashmenuturigusht = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini lavash",callback_data="mini1"),
	  InlineKeyboardButton(text="Classic lavash",callback_data="classic1"),
	  ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back9')


],
    ],
 
)

lavashmenuturitovuq = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini lavash",callback_data="mini2"),
	  InlineKeyboardButton(text="Classic lavash",callback_data="classic2"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back9')


],
    



],
)
lavashmenuturigushtpishloqli = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini lavash",callback_data="mini4"),
	  InlineKeyboardButton(text="Classic lavash",callback_data="classic4"),


    ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back9')


],


],
)
lavashmenuturitovuqpishloqli = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini lavash",callback_data="mini3"),
	  InlineKeyboardButton(text="Classic lavash",callback_data="classic3"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back9')


],
   



],
)
	


son1 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back4')


],

],

)

son2 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back5')
],],)

son3 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back6')


],

],

)

son4 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back7')
],],)
# SHAURMA
########################################
shaurmamenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🥩Go'shtli shaurma",callback_data="gusht1"),

	InlineKeyboardButton(text="🍖Tovuqli shaurma",callback_data="tovuq1"),
	],
[ InlineKeyboardButton(text="🥩🌶Go'shtli shaurma + qalampir",callback_data="gushtqalampir"),

	InlineKeyboardButton(text="🍖🌶Tovuqli shaurma + qalampir",callback_data="tovuqqalampir"),
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back8')
],],)
shaurmamenuturigusht = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini shaurma",callback_data="mini5"),
	  InlineKeyboardButton(text="Classic shaurma",callback_data="classic5"),
	  ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back15')


],
    ],
 
)

shaurmamenuturitovuq = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Mini shaurma",callback_data="mini6"),
	  InlineKeyboardButton(text="Classic shaurma",callback_data="classic6"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back15')


],
    



],
)
shaurmamenuturigushtqalampir = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🌶Mini shaurma",callback_data="mini7"),
	  InlineKeyboardButton(text="🌶Classic shaurma",callback_data="classic7"),


    ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back15')


],


],
)
shaurmamenuturitovuqqalampir = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🌶Mini shaurma",callback_data="mini8"),
	  InlineKeyboardButton(text="🌶Classic shaurma",callback_data="classic8"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back15')
], ],)

son5 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back10')


],

],

)

son6 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back11')
],],)

son7 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back12')


],

],

)

son8 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back13')
],],)
# Burger
################
burgermenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🍔Gamburger",callback_data="gamburger"),

	InlineKeyboardButton(text="🍔Chizburger",callback_data="chiz"),
	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back14')


],
],
)
burgermenuturioddiy = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Classic",callback_data="classic9"),
	  InlineKeyboardButton(text="Big burger",callback_data="big1"),
	  ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back16')


],
    ],
 
)

burgermenuturicheese = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Classic",callback_data="classic10"),
	  InlineKeyboardButton(text="Big chizburger",callback_data="big2"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back16')
],],)


son9 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back17')
],],)
son10 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back18')
],],)
# HOTDOG
############################
hotdogmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🌭Hot-Dog Baget Dabl",callback_data="dabl"),

	InlineKeyboardButton(text="🌭Classic Hot-Dog",callback_data="classic11"),
	],
[ InlineKeyboardButton(text="🌭Korolevskiy Hot-Dog",callback_data="korol"),

	InlineKeyboardButton(text="🌭Tovuqli Hot-Dog",callback_data="tovuq2"),
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back19')


],
],
)


son11 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back20')
],],)
son12 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back21')
],],)
son13 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back22')
],],)
son14 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back23')
],],)
# Sandvich
#####################
senvichmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🆑Classic sendvich club",callback_data="classic12"),

	InlineKeyboardButton(text="🍖Tovuqli sendvich",callback_data="tovuq3"),
	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back24')

],],)

son15 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back25')
],],)

son16 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back26')
],],)
# Donar
donarmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🥩Go'shtli donar",callback_data="gusht2"),

	InlineKeyboardButton(text="🍖Tovuqli donar",callback_data="tovuq4"),
	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back27')
],
],)
son17 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back28')
],],)
son18 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back29')
],],)

# Gazaklar
gazaklarmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🍟15 gram Fri",callback_data="fri"),

	InlineKeyboardButton(text="🍟Kartoshka Derevenskiy",callback_data="derevenskiy"),
	],
[ InlineKeyboardButton(text="🍚Guruch katta",callback_data="guruchkatta"),

	InlineKeyboardButton(text="🍚Guruch kichik",callback_data="guruchkichik"),
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back30')

],],)

son19 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back31')
],],)
son20 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back32')
],],)
son21 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back33')
],],)
son22 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back34')
],],)


# DESERTLAR
desertmenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🍰Assalim",callback_data="asal"),

	InlineKeyboardButton(text="🍰Qulupnay",callback_data="qulupnay"),
	],
[ InlineKeyboardButton(text="🍰Choco",callback_data="choco")
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back35')
],],)

son23 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back36')
],],)
son24 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back37')
],],)
son25 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back38')
],],)

# Pizza
pizzamenu = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="🍕Peperoni",callback_data="pizza1"),

	InlineKeyboardButton(text="🍕Ananaslik",callback_data="pizza2"),
	],
[ InlineKeyboardButton(text="🍕Margaritta",callback_data="pizza3")
	],
[ InlineKeyboardButton(text='◀️Ortga',callback_data='back39')
],],)

son26 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back40')
],],)

son27 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back41')
],],)

son28 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back42')
],],)
#######################################
# Ichimliklar

ichimlik_menyu1 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍵Choy/☕️kofe",callback_data = 'choykofe'),InlineKeyboardButton(text = "🥤Yaxna ichimliklar",callback_data = "yaxna")
    ],
    [
        InlineKeyboardButton(text = "🍸🧋Fresh/sok",callback_data = 'fresh')
    ],
    [
        InlineKeyboardButton(text = "◀️Ortga",callback_data = 'orqaga20')
    ],
  ],
)
# kofelar
ichimlik_menyu2 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "☕️Kofelar",callback_data = 'kofe'),InlineKeyboardButton(text = "🍵Choylar",callback_data = "choylar")
    ],
    [
        InlineKeyboardButton(text = "◀️Ortga",callback_data = 'orqaga6')
    ],
  ],
)

ichimlik_menyu3 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "☕️Americano",callback_data = 'americano'),InlineKeyboardButton(text = "☕️Capuchino",callback_data = "capuchino")
    ],
    [
        InlineKeyboardButton(text = "☕️Kofe 3v1",callback_data = '3v1'),InlineKeyboardButton(text = "☕️Latte",callback_data = "latte")
    ],
    [
        InlineKeyboardButton(text = "◀️Ortga",callback_data = 'orqaga7')
    ],
  ],
)

ichimlik_menyu4= InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍵Ko'k choy",callback_data = 'kuk'),InlineKeyboardButton(text = "🍵Qora choy",callback_data = "qora")
    ],
    [
        InlineKeyboardButton(text = "🍵Limon choy",callback_data = 'limon')
    ],
    [
        InlineKeyboardButton(text = "◀️Ortga",callback_data = 'orqaga13')
    ],
  ],
)





ichimlikmenuturiyaxna = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Fanta",callback_data="fanta"),
	  InlineKeyboardButton(text="Coca Cola",callback_data="cola"),],
	[ InlineKeyboardButton(text="Sprite",callback_data="sprite"),
	  InlineKeyboardButton(text="Nestle",callback_data="nestle"),],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='orqaga8')
],],)




ichmlikmenuturifresh = InlineKeyboardMarkup(

	inline_keyboard=[


	[ InlineKeyboardButton(text="Bliss sok 1L",callback_data="bliss"),
	  InlineKeyboardButton(text="Olma va Sabzi fresh",callback_data="olmasabzi"),


    ],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back48')
],],)


ichimlik_menyu5 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga10')
    ],
  ],
)

ichimlik_menyu6 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga11')
    ],
  
],
)

ichimlik_menyu7 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga12')
    ],
  ],
)


ichimlik_menyu8 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga14')
    ],
  ],
)
son30 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back57')
],],)

son31 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back58')
],],)

son32 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back59')
],],)

son33 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back60')
],],)

son34 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back61')
],],)

son35 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back62')
],],)

son36 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back63')
],],)

son37 = InlineKeyboardMarkup(

	inline_keyboard=[

[ InlineKeyboardButton(text="1",callback_data="1"),

  InlineKeyboardButton(text="2",callback_data="2"),
	
  InlineKeyboardButton(text="2",callback_data="2")


	],

	[
 InlineKeyboardButton(text="4",callback_data="4"),

  InlineKeyboardButton(text="5",callback_data="5"),
	
  InlineKeyboardButton(text="6",callback_data="6")


	],
[
 InlineKeyboardButton(text="7",callback_data="7"),

  InlineKeyboardButton(text="8",callback_data="8"),
	
  InlineKeyboardButton(text="9",callback_data="9")


	],

[ InlineKeyboardButton(text='◀️Ortga',callback_data='back64')
],],)