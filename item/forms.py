from django import forms
from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewitemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "Image", "price")
        widgets = {
            "category": forms.Select(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "Image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
        }


class EdititemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'Image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
