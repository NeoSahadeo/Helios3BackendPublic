from knox import views as knox_views
from django.urls import path
from .views import Login, PasswordCRUD, LoggedIn

urlpatterns = [
    path("loggedin", LoggedIn.as_view(), name="login"),
    path("login", Login.as_view(), name="login"),
    path("passwords", PasswordCRUD.as_view(), name="passwords"),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
