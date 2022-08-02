import sqlite3

database = sqlite3.connect('fastfood.db')
cursor = database.cursor()


def create_users_table():
    cursor.execute('''
   CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT,
        location TEXT
   )
   ''')
    # INT - INTEGER -2147483648 до 2147483648
    # BIGINT - 9223372036854775808 до 9223372036854775808
    # TINYINT -128 до 127


def create_cart_table():
    cursor.execute('''
   CREATE TABLE IF NOT EXISTS carts(
      cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER REFERENCES users(user_id) UNIQUE,
      total_products INTEGER DEFAULT 0,
      total_price DECIMAL(12, 2) DEFAULT 0
   )
   ''')


def create_cart_products_table():
    cursor.execute('''
   CREATE TABLE IF NOT EXISTS cart_products(
      cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
      cart_id INTEGER REFERENCES carts(cart_id),
      product_name TEXT,
      quantity INTEGER NOT NULL,
      final_price DECIMAL(12, 2) NOT NULL,
      
      UNIQUE(cart_id, product_name)
   )
   ''')


def create_categories_table():
    cursor.execute('''
   CREATE TABLE IF NOT EXISTS categories(
      category_id INTEGER PRIMARY KEY AUTOINCREMENT,
   category_name VARCHAR(30) NOT NULL UNIQUE
   )
   ''')


def insert_categories():
    cursor.execute('''
   INSERT OR IGNORE INTO categories(category_name) VALUES
   ('🥙 Лаваши'),
   ('🍔 Бургеры'),
   ('🌭 Хот-доги'),
   ('🥗 Салаты'),
   ('Сеты'),
   ('🍕 Пицца'),
   ('Снеки')
   ''')


def create_products_table():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products(
           product_id INTEGER PRIMARY KEY AUTOINCREMENT,
           category_id INTEGER NOT NULL,
           product_name VARCHAR(30) NOT NULL UNIQUE,
           price DECIMAL (12, 2) NOT NULL,
           description VARCHAR(150),
           image TEXT, 
           
           FOREIGN KEY(category_id) REFERENCES categories(category_id)
        );
        '''
    )


def insert_products():
    cursor.execute('''
   INSERT INTO products(category_id, product_name, price, description, image)
   VALUES
   (1, 'Мини лаваш', 20000, 'Мясо, тесто, помидоры', 'media/lavash_Mini.jpg'),
   (1, 'Лаваш', 23000, 'Мясо, тесто, помидоры', 'media/lavash_.jpg'),
   (1, 'Лаваш с сыром', 25000, 'Мясо, тесто, помидоры, сыр', 'media/lavash_SSirom.jpg'),
   (2, 'МарьИванна', 36000, 'булка, котлета из мраморной говядины, фирменный соусу салат латук, свежие помидоры, соус барбекю, капуста радичио, халапеньо', 'media/burger_MarIvanna.jpg'),
   (2, 'Тот самый', 19000, 'булка, котлета из мраморной говядины, кетчуп, соус фирменный , лук шалот , огурцы маринованные', 'media/burger_TotSamiy.jpg'),
   (2, 'Бейби бургер', 21000, 'булка, котлета из мраморной говядины, соус фирменный , латук, свежие помидоры , огурцы маринованные', 'media/burger_BabyBurger.jpg'),
   (2, 'Мяса нет', 19000, 'Стандартная булочка, Соус Фирменный, Лист Латук, Две дольки помидора, Три дольки маринованных огурцов, Две картофельной оладьи (хашбраун)', 'media/burger_MyasaNet.jpg'),
   (2, 'Местный обжора', 67000, 'булка, фирменный соус, барбекю соус, говяжий стейк, консервированный ананас, маринованные огурцы, свежие помидоры', 'media/burger_MestniyObjora.jpg'),
   (2, 'Столичный бродяга', 41000, 'булка, котлета из мраморной говядины , салат латук, маринованные огурцы, свежие помидоры, говяжий бекон,  жареные грибы с соусом демиглас, фирменный соус', 'media/burger_StolichniyBrodyaga.jpg'),
   (2, 'Крутая чика', 29000, 'булка, нежное филе курицы, карри соус, салат латук, маринованные огурцы, свежие помидоры, фирменный соус', 'media/burger_KrutayaChika.jpg'),
   (2, 'Мясоруб', 50000, 'булка, 2 котлеты из мраморной говядины , соус барбекю, сыр, свежие помидоры, маринованные огурцы, соус фирменный, салат латук', 'media/burger_Myasorub.jpg'),
   (2, 'Чизбургер', 34000, 'булка, котлета из мраморной говядины , сыр, свежие помидоры, маринованные огурцы, фирменный соус', 'media/burger_Chizburger.jpg'),
   (2, 'Розовый фламинго', 30000, 'розовая булочка, котлета из мраморной говядины , вяленые помидоры в сырном соусе, свежие помидоры, маринованные огурцы, фирменный соус, салат латук', 'media/burger_RozoviyFlamingo.jpg'),
   (2, 'Гамбургер', 31000, 'булка, говяжья котлета, свежие помидоры, маринованные огурцы, фирменный соус', 'media/burger_Gamburger.jpg'),
   (2, 'Знакомьтесь, Джо Блэк', 37000, 'чёрная булка, котлета из мраморной говядины , яйцо, болгарский перец, маринованные огурцы, свежие помидоры, арахисовая паста', 'media/burger_DjoBlack.jpg'),
   (3, 'Хот-дог Буги-вуги (острый)', 19000, 'булка, сосиска, сальса соус ,зверобой для острого хот дога', 'media/hotdog_BugiVugiOstriy.jpg'),
   (3, 'Хот-дог Буги-вуги', 19000, 'булка, сосиска, сальса соус (не острый)', 'media/hotdog_BugiVugi.jpg'),
   (3, 'Хот-дог двойной', 24000, ' булка, 2 сосиски, сальса соус', 'media/hotdog_BugiVugiDvoynoy.jpg'),
   (4, 'Салат ЦЕЗАРЬ', 27000, 'зелённый салат, помидоры, куринное филе, белый хлеб, соус Цезарь, сливочное масло, чеснок, сыр пармезан', 'media/salat_Cezar.jpg'),
   (4, 'Салат ГРЕЧЕСКИЙ', 27000, 'Оливковое масло extra virgin, лимонный сок, чеснок, сушённый орегано, морская соль, свежемолотый чёрный перец, помидоры, красный лук, огурцы, зелённый стручковый перец, сыр фета, маслины без косточек', 'media/salat_Grecheskiy.jpg'),
   (5, 'СЕТ Бургеров', 180000, 'чика бургер, столичный бродяга, чизбургер, гамбургер, фри, картофель по-деревенски, солёные огурцы', 'media/set_SetBurgerov.jpg'),
   (5, 'ХАЛЯВА 1', 52000, 'Гамбургер, Картошка Фри, Кола', 'media/set_Halyava1.jpg'),
   (5, 'ХАЛЯВА 2', 50000, 'Гамбургер, Картошка Фри, Кола', 'media/set_Halyava2.jpg'),
   (5, 'ХАЛЯВА 3', 60000, 'Гамбургер, Картошка Фри, соус, Кола', 'media/set_Halyava3.jpg'),
   (5, 'Kid`s Box', 57000, 'тот самый бургер, фри, кетчуп, сок, киндер', 'media/set_KidsBoxStrips.jpg'),
   (5, 'Шеф окрыляяяет', 64000, 'МарьИванна, Redbull ,Крисперсы', 'media/set_ShevOkrilyaet.jpg'),
   (5, 'Kid`s Box ( стрипсы )', 57000, 'Стрипсы, сок, киндер сюрприз, картофель фри, кетчуп', 'media/set_KidsBoxStrips.jpg'),
   (6, 'Пицца «Московская»', 192000, 'мясо говядины, шампиньоны, фирменный соус, сыр Хохланд, сыр гауда, сыр моцарелла', 'media/pizza_Moskovskaya.jpg'),
   (6, 'Пицца «Оливия»', 162000, 'ветчина из говядины, кукуруза консервированная, оливки зелёные, фирменный соус, сыр гауда, сыр бейби-моцарелла', 'media/pizza_Oliviya.jpg'),
   (6, 'Пицца «American BBQ»', 144000, 'телятина, приготовленная по традиционному американскому рецепту, фасоль красная, красный лук, пикантный соус, сыр гауда, сыр моцарелла', 'media/pizza_AmericanBBQ.jpg'),
   (6, 'Пицца «Болоньезе»', 194000, 'фарш из говядины, охотничьи колбаски, шампиньоны, болгарский перец, соус Бешамель, сыр пармезан, сыр гауда', 'media/pizza_Bolonyezze.jpg'),
   (6, 'Пицца «Куатро Стаджиони» (Четыре сезона)', 155000, 'классическая пицца, состоящая из четырёх частей с разными ингредиентами – четверть с шампиньонами, четверть с охотничьими колбасками, четверть с томатами, четверть с ветчиной из говядины, и всё под слоем сыра гауда и моцарелла', 'media/pizza_KuatroStadjioni.jpg'),
   (6, 'Пицца «Большая Восьмёрка»', 193000, '8 самых популярных вкусов в одной большой пицце (только 45 см)', 'media/pizza_BolshayaVosmerka.jpg'),
   (6, 'Пицца «Морской Пир»', 299000, 'лосось, морской коктейль из креветок, мидий и кальмаров, лайм, укроп, фирменный соус, сыр гауда, сыр моцарелла', 'media/pizza_MorskoyPir.jpg'),
   (6, 'Пицца «Хантер»', 79000, 'охотничьи колбаски, куриное филе, шампиньоны, огурцы маринованные, фирменный соус, сыр гауда, сыр моцарелла', 'media/pizza_Hunter.jpg'),
   (6, 'Пицца «От Шефа»', 190000, 'полузакрытая пицца с начинкой из куриного филе, копчёной говядины, охотничьих колбасок, говяжьей ветчины, томатов, сыра гауда, сыра моцарелла', 'media/pizza_OtSheffa.jpg'),
   (6, 'Пицца «Суприм»', 125000, 'салями говяжья, шампиньоны, ветчина говяжья, маслины, фирменный соус, сыр гауда, сыр моцарелла', 'media/pizza_Supreme.jpg'),
   (7, 'Картофель ФРИ', 16000, 'Картошка Фри', 'media/sneki_Fri'),
   (7, 'Сырные подушечки', 19000, 'Сырные подушечки, В порции 5шт', 'media/sneki_SirniePodushechki.jpg'),
   (7, 'Картофель ПО-ДЕРЕВЕНСКИ', 16000, 'Картофель по деревенски', 'media/sneki_KartofelPoDerevenski.jpg')
   ''')


def create_orders_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT,
            cart_id INTEGER REFERENCES carts(cart_id),
            text TEXT,
            price TEXT,
            status TEXT NOT NULL DEFAULT 'nready'
        )
    ''')


create_users_table()
create_cart_table()
create_cart_products_table()
create_categories_table()
insert_categories()
create_products_table()
insert_products()
create_orders_table()


database.commit()
database.close()
