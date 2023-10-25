from django.shortcuts import render
from django.http import HttpResponse

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
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET["servings"]) if "servings" in request.GET else 1
    recipe = DATA.get('omlet', {})
    adjusted_recipe = {key: value * servings for key, value in recipe.items()}
    response_str = "\n".join([f"{key}: {value}" for key, value in adjusted_recipe.items()])
    return HttpResponse(response_str, content_type="text/plain; charset=utf-8")

def pasta(request):
    servings = int(request.GET["servings"]) if "servings" in request.GET else 1
    recipe = DATA.get('pasta', {})
    adjusted_recipe = {key: value * servings for key, value in recipe.items()}
    response_str = "\n".join([f"{key}: {value}" for key, value in adjusted_recipe.items()])
    return HttpResponse(response_str, content_type="text/plain; charset=utf-8")

def buter(request):
    servings = int(request.GET["servings"]) if "servings" in request.GET else 1
    recipe = DATA.get('buter', {})
    adjusted_recipe = {key: value * servings for key, value in recipe.items()}
    response_str = "\n".join([f"{key}: {value}" for key, value in adjusted_recipe.items()])
    return HttpResponse(response_str, content_type="text/plain; charset=utf-8")