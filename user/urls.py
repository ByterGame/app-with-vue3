from django.urls import path
from .views import UserRegisterView, login_user, updateMoney, updateHero

urlpatterns = [
    path('register/', UserRegisterView, name='register'),
    path('login/', login_user, name='login'),
    path('updateMoney/', updateMoney, name='update_money'),
    path('updateHero/', updateHero, name='update_hero'),
]
