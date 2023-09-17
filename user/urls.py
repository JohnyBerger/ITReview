from django.urls import path, include
from user.views import UserApiView

urlpatterns = [
    path('user', UserApiView.as_view())
]
