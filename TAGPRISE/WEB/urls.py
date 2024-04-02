from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_user, name='edit_profile'),
    path('delete/', views.delete_user, name='delete_user'),
    path('item_select/', views.item_select, name='item_select')
]