from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.newfunction,name=''),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('registersuc',views.registersuc,name='registersuc'),
]