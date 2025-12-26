(+) Завдання 1.1. Вхід до GitHub 
Відкрий браузер і перейди за адресою https://github.com.
Якщо ти не ввійшов в аккаунт:
- у правому верхньому куті натисни кнопку Sign in
- введи свій логін або email від GitHub
- введи пароль і натисни кнопку Sign in 

(+) Завдання 1.2. Створення нового репозиторію 
Увійшовши в GitHub, у правій частині зверху знайди кнопку з плюсом (+) або кнопку New. Натисни на плюс (+) і вибери пункт New repository.

(+) Завдання 1.3. Налаштування репозиторію 
У полі Repository name введи назву: python-analytics-homework. Переконайся, що нижче обрано тип репозиторію Public. Знайди пункт Initialize this repository with і постав галочку біля Add a README file. Прокрути сторінку вниз і натисни зелену кнопку Create repository.

(+) Завдання 1.4. Копіювання адреси репозиторію 
Після створення репозиторію знайди зелену кнопку Code(зазвичай вона ліворуч над списком файлів). Натисни кнопку Code, переконайся, що вгорі в цьому вікні обрано вкладку HTTPS. У полі з адресою виду https://github.com/твій_нік/python-analytics-homework.git натисни на іконку копіювання.

Крок 2. Клонування репозиторію в PyCharm

( ) Завдання 2.1. Запуск процесу клонування 
Запусти PyCharm. Якщо при запуску PyCharm показує стартове вікно, натисни кнопку Get from VCS або Get from Version Control. Якщо PyCharm відкрив відразу якийсь інший проєкт, то у верхньому меню натисни File і вибери пункт New Project from Version Control або Get from Version Control.

( ) Завдання 2.2. Вставлення адреси репозиторію 
У вікні Get from Version Control у полі URL натисни Ctrl+V (або Cmd+Vна Mac), щоб вставити скопійовану HTTPS-адресу репозиторію GitHub. У полі Directory PyCharm сам запропонує папку для проєкту - можна залишити як є. Натисни кнопку Clone.

( ) Завдання 2.3. Завершення клонування 
PyCharm запитає підтвердження відкриття нового проєкту - натисни Yesабо OK. Дочекайся, поки проєкт завантажиться. Зліва має з'явитися панель Project, а в ній – папка python-analytics-homework з файлом README.md.

Крок 3. Створення файлу analysis.py і перший коміт у main

( ) Завдання 3.1. Створення Python файлу У лівій панелі Project знайди папку python-analytics-homework. Натисни правою кнопкою миші на назві папки, наведи курсор на пункт New і в підменю натисни Python File. Введи назву файлу: analysisі натисни Enter.

( ) Завдання 3.2. Додавання коду 
У відкритий пустий файл analysis.py встав наступний код:
  import pandas as pd
  
  data = { "city": [ "Kyiv", "Lviv", "Odesa" ], "sales": [ 1200, 900, 500 ] }
  df = pd.DataFrame(data)
  print( "Продажі по містах:" )
  print( df )
  print( f"Середнє значення: { df[ "sales" ].mean() }" )

Збережи файл, натиснувши Ctrl+S (або Cmd+S на Mac).

( ) Завдання 3.3. Перший коміт 
У верхньому меню PyCharm натисни Git і вибери пункт Commit. У панелі Commit переконайся, що біля файлу analysis.py стоїть галочка. У полі Commit Message введи текст: added analysis file. Натисни кнопку Commit and Push.
Якщо бачиш лише кнопку Commit, то натисни Commit, а потім знову у верхньому меню вибери Git → Push.

( ) Завдання 3.4. Авторизація (опціонально) 
Якщо PyCharm вперше робить push на GitHub, він може запитати авторизацію. Якщо відкриється вікно входу через браузер, натисни Log in via GitHub або Log in with browser. Браузер відкриється і попросить дозволити доступ PyCharm до GitHub - натисни Authorize. Поверніся до PyCharm і дочекайся повідомлення про успішний push.
Після успіху команди push відкрий у браузері сторінку репозиторію на GitHub (https://github.com/твій_нік/python-analytics-homework) і перевір, що:
- файл analysis.py є у списку файлів;
- вкладка Code показує останній коміт з повідомленням add analysis file. 

Крок 4. Сценарій 1: прийняття змін через Pull Request

( ) Завдання 4.1. Створення гілки для прийнятих змін 
Переконайся, що в PyCharm ти на гілці main (у правому нижньому куті є напис Git: main). Натисни на Git: main і в меню вибери New Branch. У полі Branch name введи: feature/update-sales-accepted. Переконайся, що встановлена опція Checkout branch і натисни Create.

( ) Завдання 4.2. Внесення змін у файл 
Відкрий файл analysis.py і знайди рядок:
  data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 900, 500]}

Заміни 900 на 950, щоб вийшло:
  data = { "city": [ "Kyiv", "Lviv", "Odesa" ], "sales": [ 1200, 950, 500 ] }

Збережи файл (Ctrl+S або Cmd+S).

( ) Завдання 4.3. Коміт і push змін 
У верхньому меню натисни Git і вибери Commit. Переконайся, що біля analysis.pyстоїть галочка. У полі Commit Message введи: update Lviv sales to 950. Натисни Commit and Push і дочекайся повідомлення про успішний push.

( ) Завдання 4.4. Створення Pull Request 

Відкрий у браузері сторінку свого репозиторію на GitHub. Зверху може з'явитися жовтий блок з кнопкою Compare & pull request для гілки feature/update-sales-accepted - натисни її. Якщо блоку немає, натисни вкладку Pull requests, потім New pull request, у полі base вибери main, у полі compare вибери feature/update-sales-accepted. У полі Title введи: Update Lviv sales to 950. Натисни Create pull request.

( ) Завдання 4.5. Злиття Pull Request 
На сторінці Pull Request натисни зелену кнопку Merge pull request, потім Confirm merge. Після злиття натисни кнопку Delete branch, щоб видалити гілку feature/update-sales-accepted на GitHub.

( ) Завдання 4.6. Підтягування змін у PyCharm 
У PyCharm переключись на main (натисни в правому нижньому куті на назву гілки і вибери main). У верхньому меню вибери Git → Pull і дочекайся завершення операції. Тепер файл analysis.py у гілці main має містити sales: [1200, 950, 500].

Крок 5. Сценарій 2: відхилення змін без злиття

( ) Завдання 5.1. Створення гілки для відхилених змін 
Переконайся, що ти на main у PyCharm. Створи нову гілку feature/update-sales-rejected (натисни Git: main в правому нижньому куті, вибери New Branch, введи назву і натисни Create).

( ) Завдання 5.2. Тимчасові зміни у файлі 
Відкрий analysis.py, знайди рядок:
  print( "Продажі по містах:" )

І заміни його на:
  print( "Продажі по містах (тимчасова версія):" )

Збережи файл.

( ) Завдання 5.3. Коміт і push 
Виконай Git → Commit, у поле Commit Message введи: temporary title change. Натисни Commit and Push і дочекайся успішного push.

( ) Завдання 5.4. Створення Pull Request 
Відкрий репозиторій на GitHub, перейди у вкладку Pull requests, натисни New pull request. У полі base обери main, у полі compare обери feature/update-sales-rejected. У полі Title введи: Temporary title change. Натисни Create pull request.

( ) Завдання 5.5. Відхилення Pull Request 
На сторінці Pull Request знайди кнопку Close pull request (зазвичай вона сіра) і натисни її. Підтверди закриття. Статус Pull Request зміниться на Closed - зміни НЕ потрапили в гілку main.

( ) Завдання 5.6. Видалення гілки 
У репозиторії на GitHub перейди у вкладку Code, натисни на напис main і обери View all branches. Знайди гілку feature/update-sales-rejected і натисни біля неї кнопку видалення (іконку кошика), підтверди видалення.

Крок 6. Сценарій 3: відкочування коміту через revert

( ) Завдання 6.1. Створення гілки для нових змін 
Переконайся, що ти на main у PyCharm. Створи нову гілку feature/add-average-comment.

( ) Завдання 6.2. Додавання коментаря 
Відкрий analysis.py і знайди рядок:
  print( f"Середнє значення: { df[ "sales"].mean() }" )

Заміни його на наступні рядки:
  average_sales = df[ "sales" ].mean()
  print( f"Середнє значення: { average_sales } )
  print( "Це середній рівень продажів по трьох містах" )

Переконайся, що відступи коректні, і збережи файл (Ctrl+S або Cmd+S).

( ) Завдання 6.3. Коміт і push 
Натисни Git → Commit, у поле Commit Message введи: add average sales comment. Натисни Commit and Push і дочекайся повідомлення про успішний push.

( ) Завдання 6.4. Створення і злиття Pull Request 
Відкрий репозиторій на GitHub, перейди у вкладку Pull requests → New pull request. У полі base вибери main, у полі compare вибери feature/add-average-comment. У Title введи: Add comment about average sales. Натисни Create pull request, потім Merge pull request і Confirm merge. Натисни Delete branch для видалення гілки.

( ) Завдання 6.5. Реверт коміту на GitHub 
На головній сторінці репозиторію (вкладка Code) знайди напис X commits і натисни на нього. У списку комітів знайди коміт з повідомленням add average sales comment і натисни на рядок з цим комітом. На сторінці коміту знайди кнопку Revert (зазвичай праворуч) і натисни її. GitHub відкриє форму для нового Pull Request з реверт-змінами. У полі Title можна залишити стандартний текст. Натисни Create pull request, потім Merge pull request і Confirm merge.

( ) Завдання 6.6. Підтягування реверту у PyCharm 
У PyCharm переключись на гілку main (якщо ти ще на feature/add-average-comment). У верхньому меню натисни Git → Pull і дочекайся завершення. Відкрий analysis.py і перевір, що додаткові рядки з average_sales та коментарем зникли - файл повернувся до вигляду до цього коміту.

Крок 7. Перегляд історії комітів

( ) Завдання 7.1. Історія в PyCharm 
У нижній частині вікна PyCharm знайди вкладку Git (якщо її не видно, натисни View → Tool Windows → Git). Натисни вкладку Git і перейди на вкладку Log. Тут ти побачиш список комітів, їх повідомлення, гілки, злиття (merge) і реверт-коміти. Клацнувши на будь-який коміт, можна побачити, які файли і рядки змінювались.

( ) Завдання 7.2. Історія на GitHub 
У репозиторії на вкладці Code натисни на напис X commits і переглянь список комітів, їх повідомлення, дати і авторів. Можна натиснути на будь-який коміт і побачити зміни у файлах. Щоб побачити історію конкретного файлу, відкрий файл analysis.py і у верхньому правому куті натисни кнопку History.

Вимоги до готової роботи:
- Є репозиторій python-analytics-homework на GitHub з файлом README.md
- У репозиторії є файл analysis.py з кодом на Python
- У main є перший коміт з повідомленням added analysis file
- Створено гілку feature/update-sales-accepted, зроблено зміну, коміт, Pull Request, зміни злиті (merge) в main, гілка видалена
- Створено гілку feature/update-sales-rejected, зроблено тимчасову зміну, коміт і Pull Request, Pull Request закритий без злиття
- Створено гілку feature/add-average-comment, зроблено зміни, коміт, Pull Request, зміни злиті в main, потім зроблено реверт коміту через Revert на GitHub, створено Pull Request з реверт-комітом і злито його
- У гілці main після pull у PyCharm видно кінцевий стан файлу analysis.py без тимчасових змін з rejected гілки і без закоментованого average_sales
Є не менше 4-6 комітів в історії
Надано скриншот історії комітів (з GitHub або з вікна Git → Log у PyCharm), де видно гілки, злиття (merge) та реверт 
