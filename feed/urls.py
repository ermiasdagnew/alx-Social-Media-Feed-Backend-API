from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, login_view, add_comment, like_post
from django.http import JsonResponse

# API root
def api_root(request):
return JsonResponse({"message": "API is running"})

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
path('', api_root),
path('auth/login/', login_view, name='login'),
path('', include(router.urls)),
path('posts/<int:id>/comments/', add_comment, name='add_comment'),
path('posts/<int:id>/like/', like_post, name='like_post'),
]
