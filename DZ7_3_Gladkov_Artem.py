#3 Написать скрипт, который собирает все шаблоны  из структуры файлов в одну папку templates
from pathlib import Path
def create_dirs_3(project):
    import os
    if not os.path.exists(project):
        os.mkdir(project)
        os.chdir(project)
        os.mkdir('settings')
        os.chdir('settings')
        with open('__init__.py', 'w', encoding='utf-8'):
            pass
        with open('dev.py', 'w', encoding='utf-8'):
            pass
        with open('prod.py', 'w', encoding='utf-8'):
            pass
        os.chdir('..')
        os.mkdir('mainapp')
        os.chdir('mainapp')
        os.mkdir('templates')
        with open('__init__.py', 'w', encoding='utf-8'):
            pass
        with open('models.py', 'w', encoding='utf-8'):
            pass
        with open('views.py', 'w', encoding='utf-8'):
            pass
        os.chdir('templates')
        os.mkdir('mainapp')
        os.chdir('mainapp')
        with open('base.html', 'w', encoding='utf-8'):
            pass
        with open('index.html', 'w', encoding='utf-8'):
            pass
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')

        os.mkdir('authapp')
        os.chdir('authapp')
        with open('__init__.py', 'w', encoding='utf-8'):
            pass
        with open('models.py', 'w', encoding='utf-8'):
            pass
        with open('views.py', 'w', encoding='utf-8'):
            pass
        os.mkdir('templates')
        os.chdir('templates')
        os.mkdir('authapp')
        os.chdir('authapp')
        with open('base.html', 'w', encoding='utf-8'):
            pass
        with open('index.html', 'w', encoding='utf-8'):
            pass
    else:
        print('Такой проект уже существует')
    return

create_dirs_3('my_project')

def create_templates(folder):
    import shutil
    import os
    path_folder = os.path.abspath(folder)
    try:
        os.chdir(path_folder)
        list_path_templates=[]
        for root, dirs, files in os.walk(path_folder):
            for dir in dirs:
                if dir == 'templates':
                    list_path_templates.append(root)
        templates='templates'
        for i in list_path_templates:
            try:
                i = f'{i}\{templates}'
                shutil.copytree(i,'templates',dirs_exist_ok=True) #игнор что папка уже есть
            except Exception:
                print('Что-то пошло не так...Программист только учится')
    except Exception:
        print('Запустите второй раз, структура каталогов создалась')

    return

create_templates('my_project')

#4 Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)

