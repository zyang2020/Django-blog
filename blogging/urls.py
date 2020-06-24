# blogging/urls.py
from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='blog_index'),
    # NOTE: post_id is a keyword argument for view function "detail_view"
    # so we have to put the correct keyword argument name "post_id".
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
]
