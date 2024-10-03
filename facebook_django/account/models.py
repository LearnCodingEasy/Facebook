# Page [ facebook/facebook_django/account/models.py ]
import uuid
# _______________________________________
# _______________________________________
# Profile
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):

    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    # personal_phone: رقم الهاتف الشخصي للمستخدم
    # personal_phone = models.CharField(max_length=15, blank=True, null=True)
    # public_phone: رقم الهاتف العام للمستخدم
    # public_phone = models.CharField(max_length=15, blank=True, null=True)
    # address: العنوان الخاص بالمستخدم
    # address = models.CharField(max_length=255, blank=True, default="")

    # workplace
    # workplace_company = models.CharField(max_length=255, blank=True, default="")
    # workplace_position = models.CharField(max_length=255, blank=True, default="")
    # workplace_city_town = models.CharField(max_length=255, blank=True, default="")
    # workplace_description = models.CharField(max_length=255, blank=True, default="")
    # workplace_time_period = models.DateTimeField(blank=True, null=True)

    # friends الاصدقاء
    # friends = models.ManyToManyField("self")
    # friends count عدد الاصدقاء
    # friends_count = models.IntegerField(default=0)
    #
    # people_you_may_know = models.ManyToManyField("self")
    #
    # posts_count = models.IntegerField(default=0)
    # _______________________________________
    # _______________________________________
    # Profile
    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return "https://learncodingeasy.github.io/Images/images/user/user.png"

    def get_cover(self):
        if self.cover:
            return settings.WEBSITE_URL + self.cover.url
        else:
            return "https://learncodingeasy.github.io/Images/images/user/user.png"


# class FriendshipRequest(models.Model):
#     # ثوابت تعريف حالات الطلب، تُستخدم لتحديد حالة كل طلب (إرسال، قبول، رفض)
#     SENT = "sent"
#     ACCEPTED = "accepted"
#     REJECTED = "rejected"
#     WAITING = "waiting"

#     STATUS_CHOICES = (
#         # تم إرسال الطلب
#         (SENT, "Sent"),
#         # تم قبول الطلب
#         (ACCEPTED, "Accepted"),
#         # تم رفض الطلب
#         (REJECTED, "Rejected"),
#         # منتظر الاستجابة بى القبول او الرفض
#         (WAITING, "Waiting"),
#     )

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     # created_for: حقل خارجي يربط بين هذا الطلب والمستخدم الذي تم إرسال الطلب إليه، مع تسمية للتوضيح
#     created_for = models.ForeignKey(
#         User, related_name="received_friendshiprequests", on_delete=models.CASCADE
#     )
#     # created_at: حقل يُسجل تاريخ ووقت إنشاء الطلب، حيث يُحدث تلقائيًا عند إنشاء السجل الجديد
#     created_at = models.DateTimeField(auto_now_add=True)
#     # created_by: حقل خارجي يربط بين هذا الطلب والمستخدم الذي أنشأ الطلب، مع تسمية للتوضيح
#     created_by = models.ForeignKey(
#         User, related_name="created_friendshiprequests", on_delete=models.CASCADE
#     )
#     # status: ( STATUS_CHOICES من قائمة ) حقل يُخزن فيه حالة الطلب
#     #  "sent" مع اختيار القيمة الافتراضية له كـ
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)

#     class Meta:
#         ordering = ("-created_at",)
