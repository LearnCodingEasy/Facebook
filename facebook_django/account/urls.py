# Page [ account/urls.py ]
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
    path("me/", api.me, name="me"),
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("editprofile/", api.editprofile, name="editprofile"),
    path("editpassword/", api.editpassword, name="editpassword"),
    # Suggested
    # path(
    #     "friends/suggested/",
    #     api.my_friendship_suggestions,
    #     name="my_friendship_suggestions",
    # ),
    # All Friends
    # path("friends/<uuid:pk>/", api.friends, name="friends"),
    # path("friends_accepted/<uuid:pk>/", api.friends_accepted, name="friends_accepted"),
    # path("friends_rejected/<uuid:pk>/", api.friends_rejected, name="friends_rejected"),
    # path("friends_waiting/<uuid:pk>/", api.friends_waiting, name="friends_waiting"),
    # path(
    #     "friends/<uuid:pk>/request/",
    #     api.send_friendship_request,
    #     name="send_friendship_request",
    # ),
    # path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
