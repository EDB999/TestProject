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
