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
