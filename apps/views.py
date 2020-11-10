from django.shortcuts import render


def year_archive(request):
    a_list = [
        {"ad": "ali", "not": 1},
        {"ad": "veli", "not": 2},
    ]

    context = {'year': 2012, 'article_list': a_list}

    return render(request, 'sayfa/list.html', context)



