from django.contrib import admin
from django.urls import path,include
from .views import career_list, book_session,index,success_page,session_list,add_session,session_detail
from .views import user_login, user_signup
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',index,name='index'),
    path('careers/', career_list, name='career_list'),
    path('book/', book_session, name='book_session'),
    path('success/', success_page, name='success_page'),
    path('sessions/', session_list, name='session_list'),
    path('sessions/add/', add_session, name='add_session'),
    path('sessions/<int:session_id>/', session_detail, name='session_detail'),
    path("accounts/login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]