from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name="home"),
    path('login/',login,name="login"),
    path('signup/',sign_up, name="signup"),
    path('dashboard/',dashboard, name="dashboard"),
    path('logout/',logout_view, name="logout"),
]