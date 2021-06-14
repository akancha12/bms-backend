from django.urls import re_path
from .views import TestView, UserSignupView

urlpatterns = [
    re_path(r'^test/$', TestView.as_view(), name='test'),
    re_path(r'^signup/$', UserSignupView.as_view(), name='signup'),
]
