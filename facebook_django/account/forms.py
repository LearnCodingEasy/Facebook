# Page [ account/forms.py ]
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "password1",
            "password2",
            # "address",
            # "personal_phone",
            # "public_phone",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "avatar",
            "cover",
            # "personal_phone",
            # "public_phone",
            # "address",
            # "workplace_company",
            # "workplace_position",
            # "workplace_city_town",
            # "workplace_description",
            # "workplace_time_period",
        )
