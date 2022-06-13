from django.shortcuts import render

# Create your views here.

menu = [{"title": "Администирование", "url_name": "admin"},
        {"title": "Центральный сайт", "url_name": "main"},
        {"title": "Перейти к сайту", "url_name": "index"},
        {"title": "Выйти", "url_name": "logout"}
        ]


def admin_portal(requests):
    context = {

        'menu': menu

    }

    return render(requests, "documents/base.html", context=context)