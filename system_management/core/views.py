from django.shortcuts import render


def index(resquest):
    return render(resquest, 'core/index.html')