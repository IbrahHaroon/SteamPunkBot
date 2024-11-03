from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainView, name="mainView"),
    path('about_page/', views.about_page, name='about_page'),
    path('base/', views.base, name='base'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('home/', views.home, name='home'),
    path('transition_page', views.transition_page, name='transition_page'),
    path('Tutorial_page', views.Tutorial_page, name='Tutorial_page'),
    path("welcome_page", views.welcome_page, name='welcome_page'),
]