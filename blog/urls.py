from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bloghome, name="bloghome"),
    path('blogpost/', views.blogPost, name="blogPost"),
    path('deletedposts/', views.isDeletedCheck, name="deletedposts"),
    path('cars/', views.cars, name="cars"),
    path('education/', views.education, name="education"),
    path('other/', views.other, name="other"),
    path('tech/', views.tech, name="tech"),
    path('science/', views.science, name="science"),
    path('money/', views.money, name="money"),
    path('news/', views.news, name="news"),
    path('wellness/', views.news, name="wellness"),
    path('home/', views.news, name="home"),
    path('searchDatabase/', views.searchPosts, name="searchPosts"),
    path('adfetch/' , views.ad_fetch, name= "ad_fetch"),
    path('fetchcategory/', views.fetch_category, name="fetchCategory"),
]