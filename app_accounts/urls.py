from django.urls import path
from .views import TalentSignUpView, FanSignUpView

urlpatterns = [
    path("sign-up/talent/", TalentSignUpView.as_view(), name="talent-signup"),
    path("sign-up/fan/", FanSignUpView.as_view(), name="fan-signup"),
]
