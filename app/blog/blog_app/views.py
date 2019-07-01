from django.shortcuts import render
from random import choice
# Create your views here.


def post_list(requset):
    n = ['Завер', 'Павел', 'Олег', 'Артём', 'Серёга']
    return render(requset, 'blog_app/index.html', context={'names': n})
