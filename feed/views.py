from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets, permissions
from .models import Post, Comment, Interaction
from .serializers import PostSerializer

# Login view
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Ensure demo user exists
    demo_user, created = User.objects.get_or_create(username="demo_user")
    demo_user.set_password("DemoPass123")
    demo_user.save()

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "Missing username or password"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"message": "Login successful"})


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        demo_user, _ = User.objects.get_or_create(username="demo_user")
        serializer.save(author=demo_user)


# Add comment
@csrf_exempt
def add_comment(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    comment_text = data.get("comment")
    if not comment_text:
        return JsonResponse({"error": "Missing comment"}, status=400)

    post = Post.objects.filter(id=id).first()
    if not post:
        return JsonResponse({"error": "Post not found"}, status=404)

    demo_user, _ = User.objects.get_or_create(username="demo_user")
    comment = Comment.objects.create(post=post, author=demo_user, content=comment_text)

    return JsonResponse({
        "id": comment.id,
        "post": post.id,
        "author": demo_user.username,
        "content": comment.content
    })


# Like post
@csrf_exempt
def like_post(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    post = Post.objects.filter(id=id).first()
    if not post:
        return JsonResponse({"error": "Post not found"}, status=404)

    demo_user, _ = User.objects.get_or_create(username="demo_user")
    interaction, created = Interaction.objects.get_or_create(post=post, user=demo_user)
    interaction.liked = True
    interaction.save()

    return JsonResponse({"message": "Post liked"})
