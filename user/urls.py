from django.urls import path
from .views import UserRegisterView, login_user, getData, updateData

urlpatterns = [
    path('register/', UserRegisterView, name='register'),
    path('login/', login_user, name='login'),
    # path('updateMoney/', updateMoney, name='update_money'),
    # path('updateHero/', updateHero, name='update_hero'),
    path('getData/', getData, name='get_data'),
    path('updateData/', updateData, name='update_data')
]
