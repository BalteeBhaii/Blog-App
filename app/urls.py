from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('post/<slug:slug>', views.post_page, name="post_page"),
    path('tag/<slug:slug>', views.tag_page, name="tag_page"),
    path('author/<slug:slug>', views.author_page, name="author_page"),
    path('search/', views.search_posts, name="search"),
    path('accounts/register/', views.register_user, name="register"),
    path('bookmark_post/<slug:slug>', views.bookmark_post,name="bookmark_post"),
    path('like_post/<slug:slug>', views.like_post,name="like_post"),
    path('all_bookmarked_post', views.all_bookmarked_post, name="all_bookmarked_post"),
    path('all_post', views.all_post, name="all_post"),
    path('all_liked_post', views.all_liked_post, name="all_liked_post")
]
