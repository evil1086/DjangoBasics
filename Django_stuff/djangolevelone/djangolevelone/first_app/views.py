from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'insert_me':'Hello Django Im from first_app views.py'}
    return render(request, 'first_app/index.html', context=my_dict)

