from django.urls import path

from . import views
from .views import PostListView

app_name = "blog"
urlpatterns = [
    # Page for adding a new reply
    path("new_reply/<int:post_id>/", views.new_reply, name="new_reply"),
    # Detail page for a specific post
    path("<int:post_id>/", views.post, name="post_detail"),
    # Home page
    path("", PostListView.as_view(), name="index"),
]
