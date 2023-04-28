"""djcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
import leads
from leads.models import Students
from leads.views import addStudents, delete, login
from leads.views import editStudents
from leads.views import foitites
from leads.views import login
from leads.views import logout
from leads.views import posts
from leads.views import profile
from leads.views import search
from leads.views import signup
from leads.views import home
from leads.views import delete
from leads import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('addStudents', views.addStudents, name="addStudents"),
    path('foitites/editStudents/<int:id>', views.editStudents),
    path('posts/editposts/<int:id>', views.editPosts),
    path('foitites', views.foitites, name='foitites'),
    path('registration/login', views.login),
    path('logout', views.logout, name='logout'),
    path('posts/', posts, name='posts'),
    path('profile', profile),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('foitites/delete/<int:id>', views.delete),
    path('posts/delete/<int:id>', views.delete_posts),
    path('search', views.search)

]
