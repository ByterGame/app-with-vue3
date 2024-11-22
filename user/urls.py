from django.urls import path
from .views import UserRegisterView, UserLoginView, CurrentUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('current/', CurrentUserView.as_view(), name='current_user'),
]
