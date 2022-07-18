from django.shortcuts import render


def house_create(request):
    return render(request, 'estate/house_create.html')