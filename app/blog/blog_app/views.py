from django.shortcuts import render
from random import choice, shuffle

def post_list(requset):
    names = ['Завер', 'Павел', 'Олег', 'Артём', 'Серёга']
    colors = [
        'text-primary', 
        'text-info', 
        'text-warning', 
        'text-danger',
        'text-success']
    shuffle(colors) 
    shuffle(names)
    values = dict(zip(colors, names))
    random_name = choice(names)
    return render(requset, 'blog_app/index.html', 
        context={
        'random_name': random_name,
        'values': values
        #'names': names,
        #'color': color
        })
