from django.contrib import admin
from django.urls import path

from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupPage,name="signupage"),
    path('login/', views.loginPage,name="loginpage"),
    path('home', views.home,name="homepage"),
    path('add/', views.addPage,name="addpage"),
    # path('edit/', views.editPage,name="editpage"),
    path('updatepage/<str:id>', views.updatepage, name="updatepage"),
    path('deletePage/<str:id>', views.deletePage, name="deletePage"),
]
