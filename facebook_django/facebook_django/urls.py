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
