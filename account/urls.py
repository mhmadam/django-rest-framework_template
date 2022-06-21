from django.urls import path
from .views import RegistrationView, LoginView, ChangePasswordView, ProfileView
from knox import views as knox_views

urlpatterns = [
    path('', ProfileView.as_view(), name='user_profile'),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('changepassword/', ChangePasswordView.as_view(), name='user_change_password'),
]