1. Необходимые библиотеки:
   - pandas
   - numpy
   - scikit-learn
   - pyTelegramBotAPI
   - gunicorn
   - Что-то мог забыть, но питон напомнит.
   Все библиотеки устанавливаются так: pip install -r requirements.txt
   Если что-то не находится, то, возможно, другое название. Поищи <название библиотеки> pypi в гугле

2. Необходимо настроить nginx. Это на твоем компе. Оставляю ссылку, че надо сделать.

    `https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#step-6-testing-gunicorn-s-ability-to-serve-the-project`

3. Ссылка на бота - https://t.me/obesity_classifier_bot
4. После скачивания проекта надо оказаться в той папке, где лежит manage.py. В терминале написать python manage.py makemigrations.
    python manage.py migrate. 
    Без точек, если что
5. Запуск приложения идет с двух терминалов. 1) python manage.py runserver. 2) python manage.py bot - это кастомная
    команда. Описана в `ml/management/comands/bot.py`. Там используется библиотека для работы с телегой. 
    Везде, где написано await loop.run_in_executor - это выполнение обычных функций в асинхронном формате, иначе 
    не поддерживается. В остальном, думаю, разберешься.
    Создается объект, данные обрабатываются в методе модели, передаются в модель машинного обучения, вычисляется значение.
    Значение возвращается в функцию и выводится сообщением в телеге.


Все основное, вроде, описал. Если возникнут вопросы - пиши.
