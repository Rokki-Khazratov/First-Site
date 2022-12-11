from django.urls import path
from . import views

app_name = 'Redcup'
urlpatterns = [
    path('',views.index, name='index'),
    path('components/', views.components, name='components'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]