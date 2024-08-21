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


# "personal_phone",
# "public_phone",
# "address",
# "workplace_company",
# "workplace_position",
# "workplace_city_town",
# "workplace_description",
# "workplace_time_period",
# "get_avatar",
# "get_cover",
# "friends_count",
# "posts_count",

# class FriendshipRequestSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)

#     class Meta:
#         model = FriendshipRequest
#         fields = (
#             "id",
#             "created_by",
#         )
