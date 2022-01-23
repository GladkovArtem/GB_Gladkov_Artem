#1. Написать скрипт, создающий стартер (заготовку) для проекта со структурой папок.

import os

def create_dirs(project):
    if not os.path.exists(project):
        os.mkdir(project)
        os.chdir(project)
        os.mkdir('settings')
        os.mkdir('mainapp')
        os.mkdir('adminapp')
        os.mkdir('authapp')
    else:
        print('Такой проект уже существует')
    return

create_dirs('my_project2')