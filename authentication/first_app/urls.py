from django.urls import path, re_path
from django.shortcuts import redirect
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.pass_change, name='passchange'),
    path('pass_change2/', views.pass_change2, name='passchange2'),
     re_path(r'^.*$', lambda request: redirect('login')),
]

