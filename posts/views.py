from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    """
    Lists all posts (latest first) and allows authenticated users to create posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author as the logged-in user
        serializer.save(author=self.request.user)
