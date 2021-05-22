from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:pk>/', views.retrieve, name='retrieve'),
    path('register', views.reqister, name='register'),
    path('login', views.loginView, name='login'),
    path('register', views.reqister, name='register'),
    # path('landing', views.landing, name='landing'), # Daniyar
    path('add_post', views.add_post, name='add_post'), # Arli
    path('user/<int:pk>/', views.user, name='user'), # Bakdoolot
    path('search', views.search, name='search'),  # Ainura
    #path('contact', views.contact, name='contact'), # Askat
    #path('404', views.not_found, name='not_found') # Akim
]