from django.shortcuts import render


# Create your views here.

menu = [{"title": "Администирование", "url_name": "admin"},
        {"title": "Центральный сайт", "url_name": "main"},
        {"title": "Перейти к сайту", "url_name": "index"},
        {"title": "Выйти", "url_name": "logout"}
        ]


def admin(requests):

    test = [{"test":"Пользователи","url":"admin"},
            {"test": "Логи авторизации", "url": "admin"}
            ]

    context = {

        'menu': menu,
        "test": test

    }
    return render(requests,"admin/1.html",context=context)
