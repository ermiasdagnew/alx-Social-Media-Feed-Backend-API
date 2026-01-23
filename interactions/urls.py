from django.urls import path
from .views import LikeCreateView, CommentListCreateView

urlpatterns = [
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
