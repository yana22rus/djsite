from django.shortcuts import render

# Create your views here.

menu = [{"title": "Администирование", "url_name": "admin"},
        {"title": "Центральный сайт", "url_name": "main"},
        {"title": "Перейти к сайту", "url_name": "index"},
        {"title": "Выйти", "url_name": "logout"}
        ]


def main_site(requests):
    side_bar = [{"title": "Новости", "url": "news"},
                {"title": "Документы", "url": "documents"},
                {"title": "Теги новостей", "url": "documents"},
                {"title": "Теги документов", "url": "documents"},
                {"title": "Фоторепортажи", "url": "documents"},
                {"title": "Видеорепортажи", "url": "documents"},
                ]

    context = {

        'menu': menu,
        "side_bar": side_bar

    }
    return render(requests, "main/main.html", context=context)
