from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # додати уставні URL автентифікації
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]