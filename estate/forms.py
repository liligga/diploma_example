from django import forms
from .models import House, HouseDetail, HouseImage


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('title', 'latitude', 'longitude')


class DetailForm(forms.ModelForm):
    class Meta:
        model = HouseDetail
        fields = ( 'number_of_bedrooms', 'floor_number')


class ImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ('file',)
