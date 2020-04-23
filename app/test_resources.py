from random import random

from app.resources import ResourcesAbstract


def uni_id(n):
    return int(random() * 10 ** n)


def rand_status():
    map_status = ['active', 'proposed', 'closed', 'resolve']
    i = int(random() * 4)
    return map_status[i]


class TestResources(ResourcesAbstract):

    async def get_projects(self):
        return [
            {'value': 'true', 'id': 12353223, 'name': 'Проект "Альфа"'},
            {'value': 'false', 'id': 32132453, 'name': 'Проект "Бетта"'},
            {'value': 'false', 'id': 23234523, 'name': 'Проект "Ганна"'},
            {'value': 'false', 'id': 32034543, 'name': 'Cupcake'},
            {'value': 'false', 'id': 11254323, 'name': 'Gingerbread'},
            {'value': 'false', 'id': 32212343, 'name': 'Jelly bean'},
            {'value': 'false', 'id': 23153432, 'name': 'Lollipop'},
            {'value': 'false', 'id': 74554322, 'name': 'Honeycomb'},
            {'value': 'false', 'id': 34654212, 'name': 'KitKat'},
            {'value': 'false', 'id': 23454312, 'name': 'Проект "Бисмарк"'},
            {'value': 'false', 'id': 23554322, 'name': 'Проект "Айова"'},
        ]

    async def get_tasks(self, project_id, group):
        data = {
            '12353223': {
                'analysis': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'architecture': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'development': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'testing': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'support': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ]
            },
            '32132453': {
                'analysis': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'architecture': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'development': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'testing': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 2 Project Betta',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ],
                'support': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 1 Project Alpha',
                     'status': rand_status()},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Task Alpha Stage 3 Project Gamma',
                     'status': rand_status()}, ]
            }
        }
        return data[project_id][group]

    async def get_requirements(self, project_id, group):
        data = {
            '12353223': {
                'analysis': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'architecture': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'development': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'testing': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'support': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ]
            },
            '32132453': {
                'analysis': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'architecture': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'development': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'testing': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 2 Project Betta'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ],
                'support': [
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 1 Project Alpha'},
                    {'value': 'false', 'id': uni_id(6), 'name': 'Req Alpha Stage 3 Project Gamma'}, ]
            }
        }
        return data[project_id][group]

    async def get_command(self, project_id, group):
        data = {
            '12353223': {
                'analysis': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'},
                ],
                'architecture': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Колотушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'development': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'testing': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'support': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ]
            },
            '32132453': {
                'analysis': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'},
                ],
                'architecture': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'development': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'testing': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ],
                'support': [
                    {'value': 'false', 'id': 3342, 'name': 'А. С. Пушкин ', 'role': 'Руководитель проектов'},
                    {'value': 'false', 'id': 3332, 'name': 'Л. Н. Толстой ', 'role': 'Тимлид'},
                    {'value': 'false', 'id': 3346, 'name': 'М. Горький ', 'role': 'Ведущий разработчик'},
                    {'value': 'false', 'id': 3442, 'name': 'А. П. Чехов ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3321, 'name': 'А. Н. Толстой ', 'role': 'Старший разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'Н. В. Гоголь ', 'role': 'Разработчик'},
                    {'value': 'false', 'id': 3344, 'name': 'А. А. Блок ', 'role': 'Тестировщик'},
                    {'value': 'false', 'id': 3344, 'name': 'Б. Л. Пастернак ', 'role': 'Интегратор'}, ]
            }
        }
        return data[project_id][group]

    async def get_plot_data(self, project_id, group):
        tasks = await self.get_tasks(project_id, group)
        over = len(tasks)
        active = round(len(list(filter(lambda x: x.get('status') == 'active', tasks))) * 100 / over + 0.5)
        proposed = round(len(list(filter(lambda x: x.get('status') == 'proposed', tasks))) * 100 / over + 0.5)
        resolve = round(len(list(filter(lambda x: x.get('status') == 'resolve', tasks))) * 100 / over + 0.5)
        closed = round(len(list(filter(lambda x: x.get('status') == 'closed', tasks))) * 100 / over + 0.5)

        if sum([active, proposed, resolve, closed]) > 100:
            active = 100 - sum([proposed, resolve, closed])
        data = [
            {'label': 'Active', 'value': active, 'color': 'blue'},
            {'label': 'Proposed', 'value': proposed, 'color': 'orange'},
            {'label': 'Resolve', 'value': resolve, 'color': 'green'},
            {'label': 'Closed', 'value': closed, 'color': 'gray'}
        ]
        return data
