from django.db import models
from django.conf import settings
from posts.models import Post

User = settings.AUTH_USER_MODEL

class Like(models.Model):
    """
    Represents a like on a post by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"

class Comment(models.Model):
    """
    Represents a comment on a post by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.id}"
