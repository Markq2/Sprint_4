Qa python final sprint. 

Project for UI tests on Яндекс.Самокат app

Files structure:
```commandline
Sprint_4/
    |-- data/ - директория для тестовых данных  
    |    |-- data.py - файл с используемыми в тестах данными
    |-- helpers/ директория со вспомогательными функциями  
    |    |-- helpers.py - файл с вспомогательными функциями
    |-- locators/ директория для локаторов
    |    |-- locators.py - файл с локатороами, разбиты на классы по страницам
    |-- pages/ директория для методов, разбиты по страницам
    |    |-- base_page.py - базовые методы использующиеся на всех страницах
    |    |-- main_page.py -  методы использующиеся на главной странице
    |    |-- order_page.py - методы использующиеся на странице оформления заказа
    |-- tests/ директория для тестов, разбиты по страницам
    |    |-- test_main_page.py - тесты на главной странице
    |    |-- test_order_page.py - тесты на странице оформления заказа   
    |-- .gitignore.py - описание файлов, которые не нужно добавлять в git
    |-- conftest.py - файл для фикстур
    |-- README.md - описание проекта    
    |-- requirements.txt - файл с зависимостями, используемыми на проекте
```

Dependencies:

Перечислены в requirements.txt:

 - allure-pytest==2.13.2
 - allure-python-commons==2.13.2
 - attrs==23.1.0
 - certifi==2023.7.22
 - exceptiongroup==1.1.3
 - h11==0.14.0
 - idna==3.4
 - iniconfig==2.0.0
 - outcome==1.2.0
 - packaging==23.1
 - pluggy==1.2.0
 - PySocks==1.7.1
 - pytest==7.4.0
 - selenium==4.11.2
 - sniffio==1.3.0
 - sortedcontainers==2.4.0
 - trio==0.22.2
 - trio-websocket==0.10.3
 - urllib3==2.0.4
 - wsproto==1.2.0


Tests:

test_main_page:
-   test_check_answers_on_main_page - проверка ответов на "Вопросы о важном" на главной
-   test_open_yandex_by_click_on_logo - проверка перехода на страницу Яндекс.Дзен по логотипу

test_order_page:
-   test_open_samokat_main_page_by_click_on_logo - проверка  перехода на главную страницу приложения по логотипу
-   test_success_order_by_buttons_with_different_colors - проверка успешного заказа при клике по разным кнопкам Заказать, выбирая разные цвета
