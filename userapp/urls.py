from .import views
from django.urls import path

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
    path('profile/<int:id>',views.Profile,name='profile'),

]