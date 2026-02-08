# Тестовое Задание
Задача - написать скрипт который обрабатывает данные из csv файла, затем выводит отчет по запросу в виде таблицы. 
     
Скачать проект:  
`git clone https://github.com/Kadina1988/test_z.git`  
Создать и активировать виртуальное окружение:  
`python venv venv`  
`source venv/bin/activate`  
Установить зависимости:  
`python -m pip install -r requirements`  
  
Пример запуска скрипта:  
`python script.py 'files/economic1.csv' 'files/economic2.csv' --report='population'`  
Можно добавлять один или несколько csv файлов.

Запуск тестов:  
`pytest tests/test_script.py`





