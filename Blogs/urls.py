from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home"),
    path('deleteBlog/<str:pk>/',views.deleteBlog,name="deleteBlog"),
    path('CreateBlog', views.CreateBlog, name="CreateBlog"),
    path('EditBlog/<str:pk>/', views.EditBlog, name="EditBlog"),
    path('ViewBlog/<str:pk>/', views.ViewBlog, name="ViewBlog"),
]