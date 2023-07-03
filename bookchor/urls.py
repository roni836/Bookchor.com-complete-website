from django.contrib import admin
from django.urls import path,re_path,include
from cb.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path("news/",viewBook, name="viewBook"),
    path("generous/<int:id>/",filterGenerous, name="filterGenerous"),
    path("delete/",deleteBook, name="deleteBook"),
    path("insert/",addBook, name="addBook"),
    path("login/",signIn, name="signIn"),
    path("logout/",signOut, name="signOut"),
    path("register/",signUp, name="signUp"),
    path("edit/",editBook, name="editBook"),
    path("search/",searchBook, name="search"),
    re_path('^', include('django.contrib.auth.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)