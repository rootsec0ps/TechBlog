from django.urls import path

from .views import PostListView, PostDetailView

app_name = "blog"
urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
]