# Page [ account/models.py ]
# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين.
import uuid

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع.
from django.conf import settings

# AbstractBaseUser, PermissionsMixin: لإنشاء نموذج مستخدم مخصص.
# UserManager: لإدارة إنشاء المستخدمين.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# models: لإنشاء نماذج Django.
from django.db import models

# timezone: للتعامل مع التوقيتات.
from django.utils import timezone


class CustomUserManager(UserManager):
    """
    _create_user دالة داخلية لإنشاء مستخدم جديد
    name: اسم المستخدم.
    email: البريد الإلكتروني للمستخدم.
    password: كلمة المرور.
    **extra_fields: أي حقول إضافية.
    """

    def _create_user(self, name, email, password, **extra_fields):
        """
        إذا لم يتم تقديم بريد إلكتروني، سيتم رفع خطأ.
        يتم تحويل البريد الإلكتروني إلى صيغة قياسية باستخدام normalize_email.
        يتم إنشاء المستخدم باستخدام self.model مع الحقول المقدمة.
        يتم تعيين كلمة المرور باستخدام set_password.
        يتم حفظ المستخدم في قاعدة البيانات باستخدام user.save.
        """
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    """
    create_user دالة لإنشاء مستخدم عادي
    name: اسم المستخدم (اختياري).
    email: البريد الإلكتروني (اختياري).
    password: كلمة المرور (اختياري).
    **extra_fields: أي حقول إضافية.
    """

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        """
        يتم تعيين is_staff و is_superuser إلى False إذا لم يتم تحديدهما في extra_fields.
        يتم استدعاء _create_user لإنشاء المستخدم.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # حقل يتم تعبئة من المستخدام
    # تسجيل الدخول
    # name: الاسم الخاص بالمستخدم
    name = models.CharField(max_length=255, blank=True, default="")
    # surname: الاسم العائلةالخاص بالمستخدم
    surname = models.CharField(max_length=255, blank=True, default="")
    # email: البريد الإلكتروني الخاص بالمستخدم
    email = models.EmailField(unique=True)
    # Date of birth تاريخ الميلاد
    date_of_birth = models.DateField(default=timezone.now)

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

    # personal_phone: رقم الهاتف الشخصي للمستخدم
    personal_phone = models.CharField(max_length=15, blank=True, null=True)
    # public_phone: رقم الهاتف العام للمستخدم
    public_phone = models.CharField(max_length=15, blank=True, null=True)
    # address: العنوان الخاص بالمستخدم
    address = models.CharField(max_length=255, blank=True, default="")

    # Gender الجنس المستخدم
    gender = models.CharField(max_length=15, blank=True, null=True)
    # workplace
    workplace_company = models.CharField(max_length=255, blank=True, default="")
    workplace_position = models.CharField(max_length=255, blank=True, default="")
    workplace_city_town = models.CharField(max_length=255, blank=True, default="")
    workplace_description = models.CharField(max_length=255, blank=True, default="")
    workplace_time_period = models.DateTimeField(blank=True, null=True)

    # friends الاصدقاء
    friends = models.ManyToManyField("self")
    # friends count عدد الاصدقاء
    friends_count = models.IntegerField(default=0)
    #
    people_you_may_know = models.ManyToManyField("self")
    #
    posts_count = models.IntegerField(default=0)

    # حقل يتم تعبئة تلقائي
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

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return "https://picsum.photos/200/200"

    def get_cover(self):
        if self.cover:
            return settings.WEBSITE_URL + self.cover.url
        else:
            return "https://picsum.photos/200/200"


class FriendshipRequest(models.Model):
    # ثوابت تعريف حالات الطلب، تُستخدم لتحديد حالة كل طلب (إرسال، قبول، رفض)
    SENT = "sent"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WAITING = "waiting"

    STATUS_CHOICES = (
        # تم إرسال الطلب
        (SENT, "Sent"),
        # تم قبول الطلب
        (ACCEPTED, "Accepted"),
        # تم رفض الطلب
        (REJECTED, "Rejected"),
        # منتظر الاستجابة بى القبول او الرفض
        (WAITING, "Waiting"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # created_for: حقل خارجي يربط بين هذا الطلب والمستخدم الذي تم إرسال الطلب إليه، مع تسمية للتوضيح
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    # created_at: حقل يُسجل تاريخ ووقت إنشاء الطلب، حيث يُحدث تلقائيًا عند إنشاء السجل الجديد
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by: حقل خارجي يربط بين هذا الطلب والمستخدم الذي أنشأ الطلب، مع تسمية للتوضيح
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )
    # status: ( STATUS_CHOICES من قائمة ) حقل يُخزن فيه حالة الطلب
    #  "sent" مع اختيار القيمة الافتراضية له كـ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)

    class Meta:
        ordering = ("-created_at",)
