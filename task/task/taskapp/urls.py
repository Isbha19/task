from django.urls import path,include
from . import views
app_name='taskapp'

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('button/', views.button, name='button'),
    path('logout/', views.logout, name='logout'),
    path('final/', views.final, name='final'),

]