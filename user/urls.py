from django.urls import path
from .views import UserRegisterView, UserRegisterView, login_user

urlpatterns = [
    path('register/', UserRegisterView, name='register'),
    path('login/', login_user, name='login'),
    # path('current/', CurrentUserView.as_view(), name='current_user'),
]
