from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('library/', views.library, name='library'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('contact/', views.contact, name='contact'),
]