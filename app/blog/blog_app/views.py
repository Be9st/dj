from django.shortcuts import render
from random import choice, shuffle
# Create your views here.


def post_list(requset):
    n = ['Завер', 'Павел', 'Олег', 'Артём', 'Серёга']
    shuffle(n)
    random_name = choice(n)
    return render(requset, 'blog_app/index.html', context={'names': n, 'random_name':random_name})
