# Facebook
👋 Hello! 🗣️ Design presentation about online Social project named “Facebook”.

🎨 Design motivation for an online Facebook project.

💖 Please click like and appreciate.

🙏 Thank you for supporting and appreciating my efforts

## Website Build


# Preview Login
![This is an image](https://raw.githubusercontent.com/learncodingeasy/Facebook/main/facebook_vue/src/assets/image/Login.png)

# Preview Signup
![This is an image](https://raw.githubusercontent.com/learncodingeasy/Facebook/main/facebook_vue/src/assets/image/Signup.png)

# Facebook
👋 Hello! 🗣️ Design presentation about online Social project named “Faceb ook”.

🎨 Design motivation for an online Facebook project.

💖 Please click like and appreciate.

🙏 Thank you for supporting and appreciating my efforts

## Website Build


### 1 Git Clone Project
```
git clone https://github.com/LearnCodingEasy/Facebook.git
``` 
__________________________________________________
### 2 Create File [ LICENSE ]
```
LICENSE
``` 
#### In Side File [ LICENSE ]
```
MIT License
Copyright (c) 2024 Hossam Rashad
```
__________________________________________________
### 3 Create Virtual Environment
```cmd
python -m venv facebook_virtual_environment
```
#### Activate Virtual Environment
```cmd
facebook_virtual_environment\Scripts\activate
```
__________________________________________________
### 4 Install Django
```cmd
pip install django
```
__________________________________________________
### 5 Install Django Libraries [ 1 - djangorestframework | 2 - djangorestframework-simplejwt | 3 - django-cors-headers | 4 - pillow ]
```cmd
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```
__________________________________________________
### 6 Create Django Project
```cmd
django-admin startproject facebook_django
```
__________________________________________________
### 7 Create Django App
```cmd
cd facebook_django
```
```python
python manage.py startapp account
```
__________________________________________________
### 8 Setup Djang Libraries
```python
# Page [facebook/facebook_django/facebook_django/settings.py]

# استيراد مكتبة timedelta عشان نحدد مدة صلاحية التوكين
from datetime import timedelta

# ALLOWED_HOSTS ده المتغير اللي بنحدد فيه الدومينات أو الآيبيهات اللي مسموح لها تشغل المشروع
ALLOWED_HOSTS = []

# URL أو على سيرفر حقيقي (localhost) الموقع اللي بنشتغل عليه سواء كان محلي
WEBSITE_URL = "http://127.0.0.1:8000"

# EMAIL_BACKEND ده اللي بيحدد طريقة إرسال الإيميلات من خلال 
# Django، هنا مختار انه يطبع الإيميلات في الكونسل
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Django، هنا سيتم إرسال الرسائل الإيميلات الى الإيميلات
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# مزود SMTP الخاص بك (في هذه الحالة Gmail)
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# البريد الإلكتروني الذي سيتم إرسال الرسائل منه
EMAIL_HOST_USER = "learncodingeasy0100@gmail.com"
# كلمة مرور البريد الإلكتروني
EMAIL_HOST_PASSWORD = "uxcg nuae kfjq txre"
DEFAULT_FROM_EMAIL = "learncodingeasy0100@gmail.com"


# AUTH_USER_MODEL ده اللي بنحدد فيه موديل المستخدمين اللي شغالين عليه
AUTH_USER_MODEL = "account.User"

# SIMPLE_JWT دي إعدادات مكتبة JWT اللي بنستخدمها لإدارة التوكينات
SIMPLE_JWT = {
    # ACCESS_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين الدخول
    # (Access Token)، هنا مدته 30 يوم
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    # REFRESH_TOKEN_LIFETIME ده اللي بيحدد مدة صلاحية توكين التحديث
    # (Refresh Token)، هنا مدته 180 يوم
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    # ROTATE_REFRESH_TOKENS ده اللي بيحدد لو التوكين بيتجدد مع كل تحديث للتوكين ولا لأ، هنا مش بيتجدد
    "ROTATE_REFRESH_TOKENS": False,
}

# REST_FRAMEWORK دي إعدادات مكتبة Django Rest Framework
REST_FRAMEWORK = {
    # DEFAULT_AUTHENTICATION_CLASSES دي اللي بتحدد نوع المصادقة الافتراضية اللي هتكون JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # DEFAULT_PERMISSION_CLASSES دي بتحدد الإذن الافتراضي اللي هو أن المستخدم لازم يكون مصدق عليه (Authenticated)
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# CORS_ALLOWED_ORIGINS دي بنحدد فيها الأصول المسموح لها تتواصل مع السيرفر بتاعنا
CORS_ALLOWED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
]

# CSRF_TRUSTED_ORIGINS دي بنحدد فيها الأصول الموثوقة اللي بنسمح لها تستخدم
# CSRF مع السيرفر
CSRF_TRUSTED_ORIGINS = [
    # أصل خاص بـ Vue.js على بورت 5173
    "http://localhost:5173",
    # أصل خاص بـ Vue.js على بورت 5174
    "http://localhost:5174",
]

# Django اللي متضافه لمشروع (Libraries) والمكتبات (Apps) دي قائمة بالتطبيقات 
INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

# 🛡️ (requests) هي عبارة عن مكونات أو طبقات بتتعامل مع الطلبات Middleware الـ
# اللي بتجيلك من المستخدمين قبل ما توصل لوجهتها النهائية في السرفر
MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

# - 🌐 `STATIC_URL` بيحدد الرابط اللي هتعرض عليه الملفات الثابتة.
STATIC_URL = "static/"
# - 📷 `MEDIA_URL` بيحدد الرابط اللي هتعرض عليه ملفات الميديا اللي بيرفعها المستخدمين.
MEDIA_URL = "media/"
# - 💾 `MEDIA_ROOT` بيحدد مكان تخزين ملفات الميديا الفعلي على جهاز السيرفر
MEDIA_ROOT = BASE_DIR / "media"
```
__________________________________________________
### 9 Setup App [ Account ]
```python
# Page [ facebook/facebook_django/account/models.py ]
# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين
import uuid

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع
from django.conf import settings

# AbstractBaseUser, PermissionsMixin: لإنشاء نموذج مستخدم مخصص
# UserManager: لإدارة إنشاء المستخدمين
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# models: Django لإنشاء نماذج
from django.db import models

# timezone: للتعامل مع التوقيتات
from django.utils import timezone

# 🔧 لإدارة المستخدمين المخصص CustomUserManager تم إنشاء كلاس باسم
# Django المتوفر افتراضيًا في UserManager وهو يرث من كلاس
class CustomUserManager(UserManager):
    """
    _create_user دالة داخلية لإنشاء مستخدم جديد
    name: اسم المستخدم
    email: البريد الإلكتروني للمستخدم
    password: كلمة المرور
    **extra_fields: أي حقول إضافية
    """

    def _create_user(self, name, email, password, **extra_fields):
        # الجزء ده بيتأكد إن الإيميل مش فاضي، ولو كان فاضي سيتم رفع خطأ
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        # ومظبوط small letters هنا بنعمل عملية تنسيق للإيميل بحيث يبقى كله
        # normalize_email باستخدام
        email = self.normalize_email(email)
        # هنا بنعمل إنشاء للمستخدم نفسه وبنمرر الاسم والإيميل وبقية الحقول الإضافية
        user = self.model(email=email, name=name, **extra_fields)
        # هنا بنعمل إعداد كلمة السر للمستخدم
        user.set_password(password)
        # database وأخيرًا هنا بنحفظ المستخدم في قاعدة البيانات باستخدام الـ
        # اللي إحنا شغالين عليها
        user.save(using=self._db)
        # وبعدين بنرجع المستخدم اللي اتعمله إنشاء
        return user

    # عشان تعمل إنشاء مستخدم عادي create_user هنا بنعرف ميثود جديدة اللي هي
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        # هنا بنحدد أن المستخدم العادي مش هيبقى
        # staff ومش هيبقى superuser
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # _create_user وبعدين بننادي على الميثود اللي عملناها فوق
        # عشان تكمل عملية الإنشاء
        return self._create_user(name, email, password, **extra_fields)

    # create_superuser هنا بنعرف ميثود جديدة اللي هي
    # superuser عشان تعمل إنشاء للمستخدم اللي هو
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        # هنا بنحدد أن المستخدم ده هيبقى
        # staff وكمان هيبقى superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # _create_user وبعدين برضه بننادي على الميثود
        # superuse عشان تكمل عملية الإنشاء بس للمستخدم اللي هو
        return self._create_user(name, email, password, **extra_fields)


        # اللي هو المستخدم User بنعمل كلاس اسمه
        # AbstractBaseUser و PermissionsMixin وده بيورث من
        # Djangoاللي فيهم أساسيات المستخدم في
        class User(AbstractBaseUser, PermissionsMixin):
            # id: اللي بيكون مفتاح أساسي للمستخدم، عشان يكون فريد لكل مستخدم UUID ده الـ
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            # ___________________
            # حقل يتم تعبئة من المستخدام
            # ___________________
            # تسجيل الدخول
            # name: الاسم الخاص بالمستخدم
            name = models.CharField(max_length=255, blank=True, default="")
            # surname: الاسم العائلةالخاص بالمستخدم
            surname = models.CharField(max_length=255, blank=True, default="")
            # email: البريد الإلكتروني الخاص بالمستخدم
            email = models.EmailField(unique=True)
            # Date of birth تاريخ الميلاد
            date_of_birth = models.DateField(default=timezone.now)
            # Gender الجنس المستخدم
            gender = models.CharField(max_length=15, blank=True, null=True)
            # avatar: الصورة الشخصية للمستخدم
            avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
            # cover: الصورة الغلاف للمستخدم
            cover = models.ImageField(upload_to="covers", blank=True, null=True)
        
            # is_active: حالة تفعيل المستخدم
            is_active = models.BooleanField(default=True)
            # is_superuser: حالة المستخدم كمشرف
            is_superuser = models.BooleanField(default=False)
            # is_staff: حالة المستخدم كموظف
            is_staff = models.BooleanField(default=False)
        
            # ___________________
            # حقل يتم تعبئة تلقائي
            # ___________________
            # date_joined: تاريخ انضمام المستخدم
            date_joined = models.DateTimeField(default=timezone.now)
            # last_login: تاريخ آخر تسجيل دخول للمستخدم
            last_login = models.DateTimeField(blank=True, null=True)
        
            # تخصيص السلوك في إدارة المستخدمين بشكل مرن ومنظم
            objects = CustomUserManager()
        
            # email يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو
            USERNAME_FIELD = "email"
            # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
            EMAIL_FIELD = "email"
            # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
            REQUIRED_FIELDS = []

# اللي هو المستخدم User بنعمل كلاس اسمه
# AbstractBaseUser و PermissionsMixin وده بيورث من
# Djangoاللي فيهم أساسيات المستخدم في
class User(AbstractBaseUser, PermissionsMixin):
    # id: اللي بيكون مفتاح أساسي للمستخدم، عشان يكون فريد لكل مستخدم UUID ده الـ
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    # تسجيل الدخول
    # name: الاسم الخاص بالمستخدم
    name = models.CharField(max_length=255, blank=True, default="")
    # surname: الاسم العائلةالخاص بالمستخدم
    surname = models.CharField(max_length=255, blank=True, default="")
    # email: البريد الإلكتروني الخاص بالمستخدم
    email = models.EmailField(unique=True)
    # Date of birth تاريخ الميلاد
    date_of_birth = models.DateField(default=timezone.now)
    # Gender الجنس المستخدم
    gender = models.CharField(max_length=15, blank=True, null=True)
    # avatar: الصورة الشخصية للمستخدم
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # cover: الصورة الغلاف للمستخدم
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # is_active: حالة تفعيل المستخدم
    is_active = models.BooleanField(default=True)
    # is_superuser: حالة المستخدم كمشرف
    is_superuser = models.BooleanField(default=False)
    # is_staff: حالة المستخدم كموظف
    is_staff = models.BooleanField(default=False)

    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    # date_joined: تاريخ انضمام المستخدم
    date_joined = models.DateTimeField(default=timezone.now)
    # last_login: تاريخ آخر تسجيل دخول للمستخدم
    last_login = models.DateTimeField(blank=True, null=True)

    # تخصيص السلوك في إدارة المستخدمين بشكل مرن ومنظم
    objects = CustomUserManager()

    # email يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو
    USERNAME_FIELD = "email"
    # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
    EMAIL_FIELD = "email"
    # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
    REQUIRED_FIELDS = []
    
    
```
```python
# Page [ facebook/facebook_django/account/serializers.py ]
# Django Rest Framework من serializers هنا بنستورد مكتبة
# JSON اللي بتساعدنا في تحويل البيانات لأنواع مختلفة زي
from rest_framework import serializers

# اللي بنستخدمه في تكوين البيانات User هنا بنستورد الموديل الخاص بـ
from .models import User

# UserSerializer بنعمل كلاس اسمه
# اللي هو هيكون مسؤول عن تحويل البيانات من وإلى شكل مناسب للاستخدام
class UserSerializer(serializers.ModelSerializer):
    # Serializer هنا بنحدد الميتا كلاس اللي بيحتوي على إعدادات الـ
    class Meta:
        # User هو موديل الـ Serializer بنحدد ان الموديل اللي هنستخدمه في الـ
        model = User
        # API بنحدد الحقول اللي عايزين نحولها أو نرجعها عند التعامل مع الـ
        fields = (
            # الخاص بالمستخدم ID الحقل ده بيخزن الـ
            "id",
            # الحقل ده بيخزن الاسم الأول للمستخدم
            "name",
            # الحقل ده بيخزن اسم العائلة للمستخدم
            "surname",
            # الحقل ده بيخزن البريد الإلكتروني للمستخدم
            "email",
            # الحقل ده بيخزن تاريخ الميلاد للمستخدم
            "date_of_birth",
            # الحقل ده بيخزن الجنس الخاص بالمستخدم
            "gender",
        )

```
```python
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

```
```python
# Page [ facebook/facebook_django/account/views.py ]

# بسيطة HTTP عشان نستخدمها في إرجاع استجابات Django من HttpResponse إستيراد دالة
from django.http import HttpResponse

# (لو احتجناها) HTML عشان نستخدمها في عرض الصفحات Django من render إستيراد دالة
from django.shortcuts import render

# إستيراد نموذج المستخدم من الموديلات
from .models import User

def activateemail(request):
    # (اللي جايين في الرابط) request من الـ ID الحصول على البريد الإلكتروني و
    email = request.GET.get("email", "")
    id = request.GET.get("id", "")
    # ( ID الإيميل و ) هنا بنتأكد إن البيانات المطلوبة موجودة
    if email and id:

        # بنجيب المستخدم من قاعدة البيانات اللي ليه الـ ID والإيميل دول
        user = User.objects.get(id=id, email=email)
        # بنفعّل حساب المستخدم
        user.is_active = True
        # بنحفظ التغييرات في قاعدة البيانات
        user.save()

        # بنرجع رد نصي بيقول إن المستخدم تم تفعيله ويقدر يسجل دخول
        return HttpResponse("The user is now activated. You can go ahead and log in!")
    else:
        # لو البيانات مش كاملة أو مش صحيحة، بنرجع رد نصي بيقول إن البارامترات غير صحيحة
        return HttpResponse("The parameters is not valid!")

```
```python
# Page [ facebook/facebook_django/account/api.py ]
# Django إستيراد إعدادات المشروع عشان نستخدمها في الكود
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
# هنا بنستورد نموذج تغيير كلمة المرور الجاهز من Django

from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
# هنا بنستورد دالة إرسال البريد الإلكتروني عشان نستخدمها في إرسال إيميل التفعيل
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد دالة إنشاء الإشعارات
# from notification.utils import create_notification

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User

# FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer

# FriendshipRequestSerializer


@api_view(["POST"])
# لا توجد فئات مصادقة مطلوبة لهذه العملية
@authentication_classes([])
# لا توجد أذونات مطلوبة لهذه العملية
@permission_classes([])
def signup(request):

    data = request.data
    # القيمة الافتراضية للرسالة هي نجاح
    message = "success"

    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        # حفظ النموذج إذا كان صالحًا واسترجاع كائن المستخدم
        user = form.save()
        # تعيين حالة المستخدم على غير نشط
        user.is_active = False
        user.save()

        url = f"{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}"

        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "learncodingeasy@yahoo.com",
            [user.email],
            fail_silently=False,
        )
        # إضافة رسالة تأكيد إرسال البريد الإلكتروني
        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # JSON إذا كان النموذج غير صالح، استرجاع الأخطاء كرسالة
        message = form.errors.as_json()

    # طباعة حالة العملية (نجاح أو الأخطاء) إلى وحدة التحكم
    print(message)

    # تحتوي على حالة العملية JSON إرجاع رسالة
    return JsonResponse({"message": message}, safe=False)


# JSON إرجاع بيانات المستخدم الحالي كاستجابة
@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "surname": request.user.surname,
            "email": request.user.email,
            "date_of_birth": request.user.date_of_birth,
            "gender": request.user.gender,
        }
    )

```
```python
# Page [ facebook/facebook_django/account/urls.py ]
# URLs عشان أستخدمهم في تعريف مسارات الـ path بستورد
from django.urls import path

# Simple JWT من مكتبة TokenObtainPairView و TokenRefreshView بستورد
# login والـ token refresh عشان أستخدمهم في الـ  DRF الخاصة بالـ
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# اللى في نفس المجلد عشان أستخدم الفيوهات اللى فيه api بستورد كل حاجة من ملف
from . import api

# هنا بقوم بتعريف كل المسارات الـ
# URLs الخاصة بالـ app دي
urlpatterns = [
    # لما يتطلب loginالمسار ده بيعرض معلومات المستخدم اللى عامل
    path("me/", api.me, name="me"),
    # المسار ده مسئول عن عملية تسجيل حساب جديد
    path("signup/", api.signup, name="signup"),
    # tokens (access و refresh) وإصدار الـ login المسار ده مسئول عن عملية الـ
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # refresh token باستخدام الـ access token المسار ده مسئول عن تجديد الـ
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```
```python
# Page [ facebook/facebook_django/facebook_django/urls.py ]
# djangoمن admin بعمل استيراد لـ
# Django عشان اقدر أستخدم لوحة التحكم الخاصة بـ
from django.contrib import admin

# URLs عشان أستخدمهم في تعريف مسارات الـ path و include بستورد
from django.urls import path, include

# بستورد الإعدادات
# `settings` و`static`
# عشان أستخدمهم في إضافة مسارات الملفات الثابتة زي الصور
from django.conf import settings
from django.conf.urls.static import static

# بستورد الفيو اللى هستخدمه لتفعيل الإيميل
from account.views import activateemail

# هنا بقوم بتعريف كل المسارات الـ
# URLs اللي الموقع هيستخدمها
urlpatterns = [
    # include وبستخدم /api/،و اللى كل حاجة فيه هتبقى تحت API مسار الـ
    # account اللى اسمها app عشان أضيف كل المسارات الخاصة بالـ
    path("api/", include("account.urls")),
    # اللي هيكون شغال لما حد يضغط على لينك التفعيل في الإيميل activateemail مسار الـ
    path("activateemail/", activateemail, name="activateemail"),
    # Django اللى بيدخلني على لوحة التحكم بتاعة admin المسار الخاص بالـ
    path("admin/", admin.site.urls),
    # ده لإضافة مسارات الملفات الثابتة زي الصور،
    #  وبيبقى شغال بس لما الموقع بيكون في وضع التطوير (development)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
__________________________________________________

### 10 Create Vue Project
```
npm create vue@latest
```
__________________________________________________

### 11 Choose Vite [ Project name & Select a framework ]
```
√ Project name: ... facebook_vue
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes
√ Add Prettier for code formatting? ... No / Yes
√ Add Vue DevTools 7 extension for debugging? (experimental) ... No / Yes

Scaffolding project in E:\Projects\Facebook\facebook_vue...

Done. Now run:
  cd facebook_vue
  npm install
  npm run format
  npm run dev
```
__________________________________________________

### 12 Go To Project [ Install & Run Dev ]
```
cd facebook_vue
npm install
npm run format
npm run build
npm run dev
```

__________________________________________________
### 13  Install Vue Libraries [ 1 - Tailwind | 2 - PrimeVue | 3 - scss | 4 - Axios | 5 - Font Awesome | 6 - Pwa | 7 -  | 8 - | 9 - |  ]
```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

npm install primevue primeicons
npm install @primevue/themes

npm install -D sass

npm install axios

npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons

npm install -D vite-plugin-pwa

npm i swiper
```
__________________________________________________

### 14 Configure Tailwind
* tailwind.config.js
```js
// Page [ facebook/facebook_vue/tailwind.config.js ]
content: [
"./index.html",
"./src/**/*.{vue,js,ts,jsx,tsx}",
],
```
* style.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

__________________________________________________

### 15 Import Font Awesome
```js
// Page [ facebook/facebook_vue/src/main.js ]
// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

app.component("fa", FontAwesomeIcon)
```


__________________________________________________
### 16 Add Pwa To Vue 
```js
// Page [ facebook/facebook_vue/vite.config.js ]

import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({ 
      // ليكون "تحديث تلقائي" Service Worker إعداد نوع التسجيل لـ 
      registerType: 'autoUpdate',
      workbox: {
        // Service Worker أنماط الملفات التي سيتم تخزينها مسبقًا في الـ 
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        // يتحكم في كل العملاء الحاليين دون الحاجة لإعادة التحميل Service Worker يجعل الـ 
        clientsClaim: true,
         //  Service Worker يتجاوز فترة الانتظار وينشط الـ 
        skipWaiting: true,
        // ولا يُنظفها Cache يُبقي على النسخ القديمة من الـ 
        cleanupOutdatedCaches: false,
        // للعمل أثناء عدم الاتصال بالإنترنت Google يتيح تحليلات 
        offlineGoogleAnalytics: true,
        // (الخرائط المصدرية) لتسهيل تتبع الأخطاء sourcemaps تفعيل 
        sourcemap: true,
        runtimeCaching: [
          {
            // أو نوع الطلبات التي سيتم تخزينها أثناء التشغيل URL تحديد نمط 
            urlPattern: ({ request }) => 
              request.destination === 'document' || 
              request.destination === 'script' || 
              request.destination === 'style' || 
              request.destination === 'image' || 
              request.destination === 'font',
            // استراتيجية التخزين المؤقت التي تعرض النسخة المخزنة مؤقتًا أثناء الحصول على نسخة جديدة من الشبكة
            handler: 'StaleWhileRevalidate',
            options: {
              // المستخدم لتخزين هذه الملفات (cache) اسم الكاش 
              cacheName: 'assets-cache',
              expiration: {
                // عدد الملفات التي يمكن تخزينها في الكاش كحد أقصى
                maxEntries: 100,
                // مدة التخزين المؤقت لهذه الملفات (30 يومًا)
                maxAgeSeconds: 60 * 60 * 24 * 30 
              }
            }
          }
        ],
      },
      devOptions: {
         // PWA تمكين خيارات التطوير أثناء تطوير 
        enabled: true
      },
      injectRegister: 'auto',
      includeAssets: ["**/*"],
      manifest: {
        name: 'Facebook',
        short_name: 'Facebook',
        description: 'My Awesome App Facebook',
        theme_color: '#ffffff',
        icons: [
                {
                  "src": "./images/icons/facebook_icon_72x72.png",
                  "type": "image/png",
                  "sizes": "72x72",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_96x96.png",
                  "type": "image/png",
                  "sizes": "96x96",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_128x128.png",
                  "type": "image/png",
                  "sizes": "128x128",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_144x144.png",
                  "type": "image/png",
                  "sizes": "144x144",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_152x152.png",
                  "type": "image/png",
                  "sizes": "152x152",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_192x192.png",
                  "type": "image/png",
                  "sizes": "192x192",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_384x384.png",
                  "type": "image/png",
                  "sizes": "384x384",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_512x512.png",
                  "type": "image/png",
                  "sizes": "512x512",
                  "purpose": "any maskable"
                }
              ],
              screenshots: [
                {
                  "src": "./images/screenshots/screenshots.png",
                  "sizes": "640x480",
                  "type": "image/png",
                  "form_factor": "wide"
                  // "form_factor": "narrow"
                }
              ]
      },
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})

```

__________________________________________________

### 17 Setup Axios
```js
// Axios
// axios استيراد
import axios from "axios"
axios.defaults.baseURL = "http://127.0.0.1:8000"

app.use(router, axios)
```

__________________________________________________
### 18 Setup PrimeVue
```js
// Page [ facebook/facebook_vue/src/main.js ]
// Prime Vue 
import PrimeVue from "primevue/config";
// Popup
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'
// Button
import Button from 'primevue/button';
// Form
import Fluid from 'primevue/fluid';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import Checkbox from 'primevue/checkbox';
import DatePicker from 'primevue/datepicker';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
// Menu
import Menubar from 'primevue/menubar';
import TieredMenu from 'primevue/tieredmenu';
// Image
import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';
// Popup
import Popover from 'primevue/popover';
import Dialog from 'primevue/dialog';
// Card
import Card from 'primevue/card';
// Theme
import Noir from './presets/Noir.js';
import ThemeSwitcher from './components/Theme/ThemeSwitcher.vue';
// Toast
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';
// Message
import Message from 'primevue/message';
// PrimeIcons أيقونات 
import 'primeicons/primeicons.css'
import 'tailwindcss/tailwind.css'

// Prime Vue 
app.use(PrimeVue, {
  theme: {
      preset: Noir,
      options: {
          prefix: 'p',
          darkModeSelector: '.p-dark',
          cssLayer: false,
      }
  }
});
app.use(ConfirmationService);
app.use(DialogService);
// Prime Theme Switcher
app.component('ThemeSwitcher', ThemeSwitcher);
// Prime Button
app.component('prime_button', Button);
// Prime Form
app.component('prime_fluid', Fluid);
app.component('prime_input_text', InputText);
app.component('prime_input_password', Password);
app.component('prime_float_label', FloatLabel);
app.component('prime_check_box', Checkbox);
app.component('prime_date_picker', DatePicker);
app.component('prime_input_group', InputGroup);
app.component('prime_input_group_addon', InputGroupAddon);
// Prime Menu
app.component('prime_menubar', Menubar);
app.component('prime_tiered_menu', TieredMenu);
app.component('prime_avatar', Avatar);
app.component('prime_avatar_group', AvatarGroup);
app.component('prime_popover', Popover);
app.component('prime_card', Card);
app.component('prime_dialog', Dialog);
// Toast
// app.use(Toast);
app.component('prime_toast', Toast);
app.use(ToastService);
// Message
// app.use(Message);
app.component('prime_message', Message);
```
* Setup Prime Theme
