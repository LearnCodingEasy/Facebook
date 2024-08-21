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

# EMAIL_BACKEND ده اللي بيحدد طريقة إرسال الإيميلات من خلال Django، هنا مختار انه يطبع الإيميلات في الكونسل
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

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
```
```python
# Page [ account/api.py ]
```
```python
# Page [ account/urls.py ]
```


