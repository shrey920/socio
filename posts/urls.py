from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts',views.PostsView.as_view(), name="allPosts"),
    path('posts/create',views.CreatePostView.as_view(), name="createPost"),
    path('posts/edit/<pk>',views.EditPostView.as_view(), name="editPost"),
    path('posts/delete/<pk>',views.DeletePostView.as_view(), name="deletePost"),
    path('posts/like/<pk>',views.LikePostView.as_view(), name="likePost"),


]
