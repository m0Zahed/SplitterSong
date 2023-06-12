from . import views
from django.urls import path

urlpatterns = [
    path("api/register", views.UserRegistrationView),
    path("api/login", views.UserLoginView),
    path('api/upload/', views.FileUploadView),
]