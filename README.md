1. Необходимые библиотеки:
   - pandas
   - numpy
   - scikit-learn
   - pyTelegramBotAPI
   - gunicorn
   - Что-то мог забыть, но питон напомнит.
   Все библиотеки устанавливаются так: pip install -r requirements.txt

Из проблем. Перед началом надо будет установить несколько вещей:
   - python3.10 (команда для linux - sudo apt-get install python3.10, для винды надо отдельно поискать)
   - sudo apt-get install python3-pip
   - sudo apt-get install python3-psycopg2

Далее надо создать виртуальную среду: python3 -m venv .venv
Вход в среду осуществляется так: source .venv/bin/activate
И здесь делать уже команду pip install -r requirements.txt
   Если что-то не находится, то, возможно, другое название. Поищи <название библиотеки> pypi в гугле

2. Ссылка на бота - https://t.me/translate_this_text_bot
3. После скачивания проекта надо оказаться в той папке, где лежит manage.py. В терминале написать
   
   python manage.py makemigrations
    python manage.py migrate
   
4. Запуск приложения идет с двух терминалов. 1) python manage.py runserver. 2) python manage.py bot - это кастомная
    команда. Описана в `ml/management/comands/bot.py`. Там используется библиотека для работы с телегой. 
    Везде, где написано await loop.run_in_executor - это выполнение обычных функций в асинхронном формате, иначе 
    не поддерживается. В остальном, думаю, разберешься.
    Создается объект, данные обрабатываются в методе модели, передаются в модель машинного обучения, вычисляется значение.
    Значение возвращается в функцию и выводится сообщением в телеге.


Все основное, вроде, описал. Если возникнут вопросы - пиши.
