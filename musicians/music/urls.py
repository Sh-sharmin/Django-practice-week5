from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/edit/<int:musician_id>/', views.musician_edit, name='musician_edit'),
    path('album/edit/<int:album_id>/', views.album_edit, name='album_edit'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
