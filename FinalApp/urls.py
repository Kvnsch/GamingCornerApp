"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LogoutView
from FinalApp import views
from FinalApp.views import *

urlpatterns = [
    path ('', views.main, name='Main'),
    path ('About/', about, name='About'),

    path ('User/Register/', views.register_user,name='Register'),
    path ('Login/', views.login_request,name='Login'),
    path ('Logout/', LogoutView.as_view(template_name="FinalApp/User/logout.html"),name='Logout'),
    path ('userEdit/', views.user_edit,name='Edit User'),

    path ('Games/NewGame/', views.addnewGame,name='Add Game'),
    path ('Games/Search/',searchHTML,name='Search'),
    path ('Games/searchResult/', views.searchResult,name='Search Result'),
    path ('Games/editGames/<releaseGame_name>',views.edit_upcomingGame,name ='Edit Game'),
    path ('Games/addReleases/',views.add_upcomingGame,name='Add Releases'),
    path ('Games/allGames/',views.list_games,name='List Games'),
   
]



