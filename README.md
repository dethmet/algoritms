# algoritms

## КАК НАЧАТЬ

Следующие команды нужно вводить в командной строке находясь в корне проекта


создаем виртуальное окружение

```
python -m venv venv
```

Активируем виртуальное окружение (для винды!!!!! на линуксе по другому)

```
source venv/Scripts/activate
```

Устанавливаем зависимости из файла requiremants.txt (рекурсивно `-r`)

```
pip install -r requirements.txt 
```

Запустить тесты

```
pytest

```

запуск файла с другой папки 

```
python examples/binary_search.py
```

