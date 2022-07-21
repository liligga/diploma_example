from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pprint import pprint
from .models import House, HouseDetail, HouseImage
from .forms import HouseForm, DetailForm, ImageForm


def house_list(request):
    houses = House.objects.all()
    context = {'houses': houses}
    return render(request, 'estate/house_list.html', context)


@login_required
def house_create(request):
    form = HouseForm()
    # images_form = ImageForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        # images_form = ImageForm(request.FILES)

        if form.is_valid():
            new_house = form.save(commit=False)
            new_house.author = request.user
            new_house.save()
            detail_form = DetailForm()
            detail_context = {'detail_form': detail_form, 'house_id': new_house.pk}
            return render(request, 'estate/partials/detail_create.html', detail_context)
    context = {'form': form}
    return render(request, 'estate/house_create.html', context)


@login_required
def detail_create(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    form = DetailForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            detail_obj = form.save(commit=False)
            detail_obj.house = house
            detail_obj.save()
            image_form = ImageForm()
            image_context = {'image_form': image_form, 'house_id': house.pk}
            return render(request, 'estate/partials/image_create.html', image_context)
    context = {'form': form, 'house_id': house.pk}
    return render(request, 'estate/partials/detail_create.html', context)


@login_required
def image_create(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.house = house
            img.save()
            return redirect('house_list')
    context = {'image_form': form, 'house_id': house.pk}
    return render(request, 'estate/partials/image_create.html', context)
