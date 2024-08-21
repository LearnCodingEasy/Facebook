# Page [ facebook/facebook_django/account/forms.py ]

# UserCreationForm خاص بإنشاء المستخدمين اللي هو Django هنا بنستورد فورم جاهز من
from django.contrib.auth.forms import UserCreationForm

# اللي بتساعدنا في إنشاء الفورمات Django من forms هنا بنستورد مكتبة
from django import forms

# app من الموديلز الخاصة بالـ User هنا بنستورد الموديل الخاص بالمستخدم اللي هو
from .models import User

# UserCreationForm اللي بيرث من SignupForm بنعمل كلاس اسمه
# الكلاس ده هيستخدم لإنشاء فورم لتسجيل المستخدمين الجدد
class SignupForm(UserCreationForm):
    # بنحدد الميتا كلاس اللي بيحتوي على إعدادات الفورم
    class Meta:
        # User بنحدد ان الموديل اللي الفورم ده هيشتغل عليه هو موديل الـ
        model = User
        fields = (
            # الاسم الأول للمستخدم
            "name",
            # اسم العائلة للمستخدم
            "surname",
            # البريد الإلكتروني للمستخدم
            "email",
            # تاريخ ميلاد المستخدم
            "date_of_birth",
            # الجنس الخاص بالمستخدم
            "gender",
            # كلمة المرور الأولى اللي المستخدم هيكتبها
            "password1",
            # تأكيد كلمة المرور اللي المستخدم هيكتبها للمطابقة
            "password2",
        )


# "address",
# "personal_phone",
# "public_phone",


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
        )


# "cover",
# "personal_phone",
# "public_phone",
# "address",
# "workplace_company",
# "workplace_position",
# "workplace_city_town",
# "workplace_description",
# "workplace_time_period",
