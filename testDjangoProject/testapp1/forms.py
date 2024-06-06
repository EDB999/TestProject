from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.core.validators import RegexValidator

from testapp1.models import BookingMachine, OrderMachine
from django import forms
from django.core.validators import RegexValidator


class BookingForm(forms.ModelForm):
    surname_validator = RegexValidator(
        regex=r'^[a-zA-Zа-яА-Я\s]*$',
        message='Enter a valid surname',
    )

    phone_number_validator = RegexValidator(
        regex=r'^\+(?:[0-9] ?){6,14}[0-9]$',
        message='Неверный формат номера телефона. Номер должен начинаться с кода страны и содержать от 6 до 14 цифр.',
        code='invalid_phone_number'
    )

    surname = forms.CharField(
        label='Фамилия',
        validators=[surname_validator],
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px; margin-bottom: 20px;'}),
    )

    phone_number = forms.CharField(
        label='Телефон',
        validators=[phone_number_validator],
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px;'}),
    )

    class Meta:
        model = BookingMachine
        fields = ['surname', 'phone_number']


# class DeliveryForm(forms.ModelForm):
#
#     def __init__(self, cost, content, *args, **kwargs):
#         super(DeliveryForm, self).__init__(*args, **kwargs)
#         self.cost = cost
#         self.content = content
#
#     street_house = forms.CharField(
#         label='Улица, дом',
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px; margin-bottom: 20px;'}),
#     )
#
#     flat_office = forms.CharField(
#         label='Кв/Офис',
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px;'}),
#     )
#
#     intercom = forms.CharField(
#         label='Домофон',
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px;'}),
#     )
#
#     entrance = forms.CharField(
#         label='Подъезд',
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px;'}),
#     )
#
#     floor = forms.CharField(
#         label='Этаж',
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 20px;'}),
#     )
#
#     def get_address(self):
#         street_house = self.cleaned_data.get('street_house', '')
#         flat_office = self.cleaned_data.get('flat_office', '')
#         intercom = self.cleaned_data.get('intercom', '')
#         entrance = self.cleaned_data.get('entrance', '')
#         floor = self.cleaned_data.get('floor', '')
#         return ' '.join(
#             ['Ул', street_house, 'Кв.', flat_office, 'Домофон', intercom, 'Подъезд', entrance, 'Этаж', floor]).strip()
#
#     def save(self, commit=True):
#         instance = super(DeliveryForm, self).save(commit=False)
#         instance.cost = self.cost
#         instance.meals = self.meals
#         instance.delivery_address = self.get_address()
#         if commit:
#             instance.save()
#         return instance
#
#     class Meta:
#         model = OrderMachine
#         fields = ['cost', 'delivery_address', 'content']