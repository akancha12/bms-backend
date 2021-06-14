from django.urls import re_path
from .views import HomeView, UserSignupView, UserLoginView

urlpatterns = [
    re_path(r"^home/$", HomeView.as_view(), name="home"),
    re_path(r"^signup/$", UserSignupView.as_view(), name="signup"),
    re_path(r"^login/$", UserLoginView.as_view(), name="login"),
]
