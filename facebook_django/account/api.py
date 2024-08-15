# Page [ account/api.py ]
# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
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
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(["POST"])
# لا توجد فئات مصادقة مطلوبة لهذه العملية
@authentication_classes([])
# لا توجد أذونات مطلوبة لهذه العملية
@permission_classes([])
def signup(request):
    """
    عملية تسجيل مستخدم جديد باستخدام بيانات الطلب المرسلة.
    تحتوي على حالة العملية (نجاح أو خطأ) JSON إرجاع رسالة
    """
    data = request.data
    # القيمة الافتراضية للرسالة هي نجاح
    message = "success"

    form = SignupForm(
        {
            "email": data.get("email"),
            "name": data.get("name"),
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
        """
        Please verify your email
        تحديد عنوان البريد الإلكتروني الذي سيتم إرساله منه
        
        # تحديد محتوى البريد الإلكتروني بما فيه رابط التفعيل
        f"The url for activating your account is: {url}",
        
        learncodingeasy@yahoo.com
        تحديد عنوان المرسل (عنوان بريد نصي) - يمكن تخصيصه بحسب الحاجة
        """
        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "learncodingeasy@yahoo.com",
            [user.email],
            fail_silently=False,
        )
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
            "personal_phone": request.user.personal_phone,
            "public_phone": request.user.public_phone,
            "address": request.user.address,
            "workplace_company": request.user.workplace_company,
            "workplace_position": request.user.workplace_position,
            "workplace_city_town": request.user.workplace_city_town,
            "workplace_description": request.user.workplace_description,
            "workplace_time_period": request.user.workplace_time_period,
            "date_of_birth": request.user.date_of_birth,
            "email": request.user.email,
            "avatar": request.user.get_avatar(),
            "cover": request.user.get_cover(),
        }
    )


@api_view(["GET"])
def profile(request, id):
    """
    عرض ملف المستخدم باستخدام رقمه الفريد.

    يقوم الفنكشن بجلب معلومات المستخدم المعرف برقم فريد، ثم يقوم بتسلسلها
    باستخدام السيريالايزر المخصص للمستخدم وإرجاعها كاستجابة JSON.
    """

    # (primary key) استرجاع معلومات المستخدم بناءً على معرفه الفريد
    user = User.objects.get(pk=id)

    # تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص
    user_serializer = UserSerializer(user)

    # JSON إرجاع البيانات كاستجابة
    return JsonResponse(
        {
            "user": user_serializer.data,
        },
        safe=False,
    )


# فقط POST يسمح له بالاستجابة لطلبات
@api_view(["POST"])
def editprofile(request):
    """
    تعديل ملف التعريف.

    الفنكشن يُستخدم لتحديث معلومات ملف التعريف الخاص بالمستخدم الحالي.
    يتم استخدام بيانات الطلب المرسلة لتحديث البريد الإلكتروني إذا كان مختلفًا عن البريد الإلكتروني الحالي.
    يتم فحص هل البريد الإلكتروني المُحدث موجود بالفعل لمستخدم آخر قبل حفظ التغييرات.
    يُنشأ نموذج ProfileForm باستخدام البيانات المُرسلة عبر POST لتحديث بيانات المستخدم.
    إذا كانت البيانات صالحة، يتم حفظ التغييرات واسترجاع بيانات المستخدم المحدثة.
    يُرجع رسالة بنجاح تحديث المعلومات وبيانات المستخدم المُحدثة.
    """

    user = request.user
    email = request.data.get("email")

    # التحقق مما إذا كان البريد الإلكتروني المحدث موجود بالفعل لمستخدم آخر
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists"})
    else:
        # إنشاء نموذج ProfileForm باستخدام البيانات المرسلة عبر POST
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            # حفظ التغييرات إذا كانت البيانات صالحة
            form.save()

        # استرجاع بيانات المستخدم المحدثة بعد التعديلات
        serializer = UserSerializer(user)

        # إرجاع رسالة بنجاح تحديث المعلومات وبيانات المستخدم المحدثة
        return JsonResponse({"message": "information updated", "user": serializer.data})


# فقط POST يسمح له بالاستجابة لطلبات
@api_view(["POST"])
def editpassword(request):
    """
    تغيير كلمة مرور المستخدم.
    يتم استدعاء الفنكشن عبر طلب POST لتغيير كلمة مرور المستخدم الحالي.
    يتم إنشاء نموذج PasswordChangeForm باستخدام البيانات المُرسلة عبر الطلب.
    في حالة صحة البيانات المُدخلة، يتم حفظ التغييرات وإرجاع رسالة بنجاح التعديل.
    إذا كان هناك أخطاء في البيانات، يتم إرجاع رسالة بالأخطاء بصيغة JSON.
    """
    # استرجاع المستخدم المتعلق بالطلب
    user = request.user

    # PasswordChangeForm إنشاء نموذج
    # باستخدام البيانات المُرسلة عبر الطلب والمستخدم الحالي
    form = PasswordChangeForm(data=request.POST, user=user)

    # التحقق من صحة البيانات المدخلة في النموذج
    if form.is_valid():
        # حفظ التغييرات إذا كانت البيانات صحيحة
        form.save()
        # حفظ التغييرات إذا كانت البيانات صحيحة
        return JsonResponse({"message": "success"})
    else:
        # إرجاع رسالة بالأخطاء التي حدثت خلال التحقق من صحة البيانات
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


@api_view(["GET"])
def friends(request, pk):
    """
    عرض قائمة الأصدقاء وطلبات الصداقة للمستخدم المحدد بواسطة معرفه (pk).
    إذا كان المستخدم هو المستخدم الحالي الذي قام بالطلب، يتم عرض طلبات الصداقة الواردة.
    يتم استخدام ملفات السيريالايزر لتحويل الكائنات إلى بيانات JSON.

    Parameters:
    - request: طلب الويب الحالي الذي يحتوي على معلومات المستخدم والطلبات.
    - pk (int): معرف المستخدم الذي يتم عرض أصدقاؤه وطلبات الصداقة.

    Returns:
    - JsonResponse: استجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، وطلبات الصداقة.
    """

    # (pk) الحصول على معلومات المستخدم بناءً على المعرف
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.SENT
        )
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def friends_accepted(request, pk):
    """
    عرض قائمة الأصدقاء وطلبات الصداقة للمستخدم المحدد بواسطة معرفه (pk).
    إذا كان المستخدم هو المستخدم الحالي الذي قام بالطلب، يتم عرض طلبات الصداقة الواردة.
    يتم استخدام ملفات السيريالايزر لتحويل الكائنات إلى بيانات JSON.

    Parameters:
    - request: طلب الويب الحالي الذي يحتوي على معلومات المستخدم والطلبات.
    - pk (int): معرف المستخدم الذي يتم عرض أصدقاؤه وطلبات الصداقة.

    Returns:
    - JsonResponse: استجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، وطلبات الصداقة.
    """

    # (pk) الحصول على معلومات المستخدم بناءً على المعرف
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.ACCEPTED
        )
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def friends_rejected(request, pk):
    """
    عرض قائمة الأصدقاء وطلبات الصداقة للمستخدم المحدد بواسطة معرفه (pk).
    إذا كان المستخدم هو المستخدم الحالي الذي قام بالطلب، يتم عرض طلبات الصداقة الواردة.
    يتم استخدام ملفات السيريالايزر لتحويل الكائنات إلى بيانات JSON.

    Parameters:
    - request: طلب الويب الحالي الذي يحتوي على معلومات المستخدم والطلبات.
    - pk (int): معرف المستخدم الذي يتم عرض أصدقاؤه وطلبات الصداقة.

    Returns:
    - JsonResponse: استجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، وطلبات الصداقة.
    """

    # (pk) الحصول على معلومات المستخدم بناءً على المعرف
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.REJECTED
        )
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def friends_waiting(request, pk):
    """
    عرض قائمة الأصدقاء وطلبات الصداقة للمستخدم المحدد بواسطة معرفه (pk).
    إذا كان المستخدم هو المستخدم الحالي الذي قام بالطلب، يتم عرض طلبات الصداقة الواردة.
    يتم استخدام ملفات السيريالايزر لتحويل الكائنات إلى بيانات JSON.

    Parameters:
    - request: طلب الويب الحالي الذي يحتوي على معلومات المستخدم والطلبات.
    - pk (int): معرف المستخدم الذي يتم عرض أصدقاؤه وطلبات الصداقة.

    Returns:
    - JsonResponse: استجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، وطلبات الصداقة.
    """

    # (pk) الحصول على معلومات المستخدم بناءً على المعرف
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.WAITING
        )
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def my_friendship_suggestions(request):
    """
    استعراض اقتراحات الصداقة للمستخدم.

    يقوم الفنكشن بإرجاع قائمة بالمستخدمين المقترحين للصداقة للمستخدم الحالي.
    يتم استخدام UserSerializer لتحويل بيانات المستخدمين إلى صيغة JSON.
    يُرجع الاستجابة ببيانات المستخدمين المقترحين بصيغة JSON مع تفعيل الأمان.
    """

    # استرجاع قائمة المستخدمين المقترحين للصداقة للمستخدم الحالي
    suggested_users = request.user.people_you_may_know.all()

    # تحويل بيانات المستخدمين إلى صيغة JSON باستخدام UserSerializer
    serializer = UserSerializer(suggested_users, many=True)

    # إرجاع الاستجابة ببيانات المستخدمين المقترحين بصيغة JSON مع تفعيل الأمان (safe=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def send_friendship_request(request, pk):
    """
    إرسال طلب صداقة.

    يقوم الفنكشن بإرسال طلب صداقة إلى المستخدم المحدد بواسطة معرفه `pk`.
    يتحقق الفنكشن من عدم وجود طلبات صداقة مرسلة بالفعل بين المستخدمين.
    في حال عدم وجود طلبات صداقة مرسلة سابقاً، يتم إنشاء طلب صداقة جديد وإرسال إشعار.
    يُرجع رسالة بنجاح إنشاء طلب الصداقة أو رسالة بأن الطلب تم إرساله بالفعل.
    """
    # print(pk)
    # استرجاع المستخدم المستهدف لإرسال طلب الصداقة إليه
    user = User.objects.get(pk=pk)

    # التحقق من وجود طلب صداقة من المستخدم المحدد للمستخدم الحالي
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )

    # التحقق من وجود طلب صداقة من المستخدم الحالي للمستخدم المحدد
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )

    # إذا لم يكن هناك طلب صداقة بين المستخدمين، قم بإنشاء طلب صداقة جديد وإرسال إشعار
    if not check1 or not check2:
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )

        # notification = create_notification(
        #     request, "new_friendrequest", friendrequest_id=friendrequest.id
        # )

        return JsonResponse({"message": "friendship request created"})
    else:
        # إذا كان هناك طلب صداقة بالفعل، قم بإرجاع رسالة بأن الطلب تم إرساله بالفعل
        return JsonResponse({"message": "request already sent"})


@api_view(["POST"])
def handle_request(request, pk, status):
    """
    معالجة طلب الصداقة.

    الفنكشن يُستخدم لمعالجة طلب الصداقة وتحديث حالته إلى الحالة المحددة بواسطة المُستخدم.
    يتم استخدام معرف المستخدم `pk` لاسترجاع المستخدم المستهدف من طلب الصداقة.
    يتم تحديث حالة طلب الصداقة إلى الحالة المُمررة `status` ويتم حفظ التغييرات.
    يتم إضافة المستخدم المحدد `request.user` إلى قائمة أصدقاء المستخدم المستهدف وتحديث عدد الأصدقاء.
    يُحدث عدد الأصدقاء أيضًا للمستخدم الحالي الذي يقوم بإرسال طلب الصداقة.
    يُنشأ إشعار باستخدام `create_notification` بنجاح معالجة طلب الصداقة.
    يُرجع رسالة بنجاح تحديث طلب الصداقة.
    """

    # استرجاع المستخدم المستهدف لمعالجة طلب الصداقة
    user = User.objects.get(pk=pk)

    # استرجاع طلب الصداقة المرتبط بالمستخدم الحالي للمستخدم المستهدف
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
        created_by=user
    )
    # تحديث حالة طلب الصداقة إلى الحالة المحددة
    friendship_request.status = status
    friendship_request.save()

    # إضافة المستخدم الحالي إلى قائمة أصدقاء المستخدم المستهدف
    user.friends.add(request.user)

    # زيادة عدد الأصدقاء للمستخدم المستهدف
    user.friends_count = user.friends_count + 1
    user.save()

    # تحديث عدد الأصدقاء للمستخدم الحالي الذي قام بإرسال طلب الصداقة
    request_user = request.user
    request_user.friends_count = request_user.friends_count + 1
    request_user.save()

    # إنشاء إشعار بنجاح معالجة طلب الصداقة
    # notification = create_notification(
    #     request, "accepted_friendrequest", friendrequest_id=friendship_request.id
    # )

    # إرجاع رسالة بنجاح تحديث طلب الصداقة
    return JsonResponse({"message": "friendship request updated"})
