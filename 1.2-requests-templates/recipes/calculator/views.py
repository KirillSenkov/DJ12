from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'hatchet_porridge': {
        'крупа, стакан': 1,
        'масло, ломтик': 1,
        'топор, шт': 1,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def menu_view(request: HttpRequest) -> HttpResponse:
    template_name = 'menu.html'
    context = {'menu': DATA,
               'dish_page': reverse('dish')}
    msg = render(request, template_name, context=context)
    return msg

def recipe_view(request: HttpRequest) -> HttpResponse:
    template_name = 'recipe.html'
    dish = request.GET.get('dish')
    context = {'recipe': DATA[dish],
               'dish': dish
    }
    msg = render(request, template_name, context=context)
    return msg

def result_view(request: HttpRequest) -> HttpResponse:
    template_name = 'result.html'
    try:
        persons = int(request.POST.get('qtty', '0'))
    except:
        persons = 0

    url = str(request)
    dish = url[url.find('?dish=')+6: len(url)-2]

    result = {}
    for name, qtty in DATA[dish].items():
        result[name] = qtty * persons
    context = {'result': result}
    return render(request, template_name, context=context)


