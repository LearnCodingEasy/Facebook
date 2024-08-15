# Page [ account/urls.py ]
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    path("me/", api.me, name="me"),
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("profile/<uuid:id>/", api.profile, name="profile"),
    path("editprofile/", api.editprofile, name="editprofile"),
    path("editpassword/", api.editpassword, name="editpassword"),
    # Suggested
    path(
        "friends/suggested/",
        api.my_friendship_suggestions,
        name="my_friendship_suggestions",
    ),
    # All Friends
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    path("friends_accepted/<uuid:pk>/", api.friends_accepted, name="friends_accepted"),
    path("friends_rejected/<uuid:pk>/", api.friends_rejected, name="friends_rejected"),
    path("friends_waiting/<uuid:pk>/", api.friends_waiting, name="friends_waiting"),
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),
    path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
