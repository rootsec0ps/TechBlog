from django.urls import path

from . import views
from .views import PostListView

app_name = "blog"
urlpatterns = [
    # Page for adding a new reply
    path("new_comment/<int:post_id>/", views.new_comment, name="new_comment"),
    # Detail page for a specific post
    path("<int:post_id>/", views.post, name="post_detail"),
    # Home page
    path("", PostListView.as_view(), name="index"),
]
