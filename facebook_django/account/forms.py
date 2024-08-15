# Page [ account/forms.py ]
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            # "personal_phone",
            # "public_phone",
            "address",
            "password1",
            "password2",
            "gender",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "avatar",
            "cover",
            "personal_phone",
            "public_phone",
            "address",
            "date_of_birth",
            "gender",
            "workplace_company",
            "workplace_position",
            "workplace_city_town",
            "workplace_description",
            "workplace_time_period",
        )
