from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.sigin, name='login'),
    path('postsign/',views.postsign, name='postsign'),
    path('welcome/', views.welcome,name='welcome' ),
]
