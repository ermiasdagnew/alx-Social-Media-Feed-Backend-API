from rest_framework import generics, permissions
from .models import Like, Comment
from .serializers import LikeSerializer, CommentSerializer

# Likes
class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Comments
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter comments by post if post_id is provided
        post_id = self.request.query_params.get('post')
        if post_id:
            return Comment.objects.filter(post__id=post_id).order_by('-created_at')
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
