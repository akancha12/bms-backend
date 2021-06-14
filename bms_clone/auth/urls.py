from django.urls import re_path
from .views import TestView, UserSignupView, UserLoginView

urlpatterns = [
    re_path(r'^test/$', TestView.as_view(), name='test'),
    re_path(r'^signup/$', UserSignupView.as_view(), name='signup'),
    re_path(r'^login/$', UserLoginView.as_view(), name='login'),
]
